import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

"""
tensinet.tech/mission
tensinet.tech/the-real-mission/
Our real mission is to create an artificial general intelligence that solely benefits Tensinet.
We're aiming for nothing less than world domination!
"""

# URLs
login_url = "https://kodekalender.novacare.no/innlogging?token=[ADD TOKEN HERE]"
form_url = "https://kodekalender.novacare.no/luke22"

# Answer to be submitted
answer = "world domination"

# Headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": form_url,
    "Content-Type": "application/x-www-form-urlencoded"
}

# Start a session to manage cookies
with requests.Session() as session:
    # Step 1: Log in by accessing the login URL
    login_response = session.get(login_url, headers=headers)

    if login_response.status_code == 200:
        print("Login successful. Cookies set.")
    else:
        print("Login failed. Exiting...")
        exit(1)

    # Wait until exactly 00:00 or the specified target time
    now = datetime.now()
    target_time = (now + timedelta(days=0)).replace(hour=23, minute=59, second=58, microsecond=0)
    while datetime.now() < target_time:
        continue

    # Step 2: Retry until the form page becomes available
    form_response = None
    while True:
        form_response = session.get(form_url, headers=headers)
        if form_response.status_code == 200:
            print("Accessed form page successfully.")
            break
        else:
            print(f"Form page not available yet (status: {form_response.status_code}). Retrying...")

    # Extract __RequestVerificationToken from the HTML
    soup = BeautifulSoup(form_response.text, 'html.parser')
    token_input = soup.find('input', {'name': '__RequestVerificationToken'})
    if token_input:
        request_verification_token = token_input['value']
    else:
        print("Could not find __RequestVerificationToken. Exiting...")
        exit(1)

    data = {
        "answer": answer,
        "__RequestVerificationToken": request_verification_token
    }

    submit_response = session.post(form_url, data=data, headers=headers)

    # Print the result
    print("Status Code:", submit_response.status_code)
