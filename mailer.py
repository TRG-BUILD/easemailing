import os
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup

EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
SERVER = 'smtp.aau.dk'
TLS_PORT = 587
HTML_TEMPLATE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "email_template.html")
EMAIL_SUBJECT = "Projekt EASE - din egen strategi"


def fetch_data():
    return {
        "situation1": "Når jeg er er stresset",
        "situation2": "Når bilen gerne vil køre hurtigere",
        "situation3": "Når jeg skal køre langt",
        "strategy1": "At bruge fartpilot eller fartbegrænser til at styre min hastighed",
        "strategy2": "At det har konsekvenser at blive taget af politiet for at køre for stærkt",
        "strategy3": "At bruge fartpilot eller fartbegrænser til at styre min hastighed",
        "strategy_text": "Just dont press that gas too much next time my good person!"
    }

def build_html_body(data: dict, template: str) -> str:
    """
    Find html template ids present in data and substitute them with data
    """
    soup = BeautifulSoup(template, 'html.parser')
    for key, text in data.items():
        elem = soup.find(id=key)
        elem.string.replace_with(text)
    return str(soup)

def build_html_message(recipient: str, subject: str, html_body: str) -> EmailMessage:
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = recipient
    msg.add_alternative(html_body, subtype='html')
    return msg

def send_mail(msg: EmailMessage) -> None:
    """
    Sends built EmailMessage object vie TLS
    """
    with smtplib.SMTP(SERVER, TLS_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)

def send_mail_localhost(msg: EmailMessage) -> None:
    """
    sends email to localhost SMTP DebuggingServer for local testing
    start server with:
    python -m smtpd -c DebuggingServer -n localhost:1025 
    """
    with smtplib.SMTP('localhost', 1025) as smtp:
        smtp.send_message(msg)

def main():
    with open(HTML_TEMPLATE_PATH, "r") as fin:
        html_template = fin.read()
    
    data = fetch_data()

    # goes to the loop for each person
    html_body = build_html_body(data, html_template)
    recipient = "msam@build.aau.dk"
    msg = build_html_message(recipient, EMAIL_SUBJECT, html_body)
    send_mail(msg)
    # log statuses?

if __name__ == "__main__":
    main()
    