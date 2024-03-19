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