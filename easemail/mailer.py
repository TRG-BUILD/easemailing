import os
import smtplib
from typing import List, Dict
from abc import ABC, abstractmethod
from email.message import EmailMessage

from bs4 import BeautifulSoup
from easemail.formatters import SurveyResult


class MailingError(Exception):
    pass


class EmailSender:
    def __init__(self, user: str, password: str, server:str, tls_port: int = 587, debug_port: int=1025):
        self.user = user
        self.password = password
        self.server = server
        self.tls_port = tls_port
        self.debug_port = debug_port

    def _send_tls(self, messages: List[EmailMessage]) -> bool:
        """
        Sends one EmailMessage object via TLS
        """
        try:
            with smtplib.SMTP(self.server, self.tls_port) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(self.user, self.password)
                for m in messages:
                    smtp.send_message(m)
        except:
            raise MailingError("Cannot send a TLS email")


    def _send_debug(self, messages: List[EmailMessage]):
        """
        sends email to localhost SMTP DebuggingServer for local testing
        start server with:
        python -m smtpd -c DebuggingServer -n localhost:1025 
        """
        success = True
        try:
            with smtplib.SMTP('localhost', self.debug_port) as smtp:
                for m in messages:
                    smtp.send_message(m)
        except:
            raise MailingError("Cannot send localhost email")

    def send(self, messages: List[EmailMessage], debug_mode=False):
        """
        Sends an email in either TLS mode ore debug
        """
        if not isinstance(messages, list):
            raise ValueError("Expected list of email.message.EmailMessage")

        if debug_mode:
            self._send_debug(messages)
        else:
            self._send_tls(messages)


class SurveyEmailBuilder(ABC):
    """
    builder for EmailMessage objects
    """
    @abstractmethod
    def build(self, survey: SurveyResult, subject: str = "") -> EmailMessage:
        """
        build an email from SurveyResult
        """


class HTMLSurveyEmailBuilder(SurveyEmailBuilder):
    def __init__(self, sender: str, html_template: str, subject: str = ""):
        self.sender = sender
        self.html_template = html_template
        self.subject = subject

    def _insert_to_html(self, survey: SurveyResult) -> str:
        """
        Find html template ids present in data and substitute them with data
        """
        data = {}
        data.update(survey.get_response_dict())
        data.update(survey.get_situation_dict())

        soup = BeautifulSoup(self.html_template, 'html.parser')
        for key, text in data.items():
            if elem := soup.find(id=key):
                elem.string.replace_with(text)
        return str(soup)

    def _build_html_message(self, recipient: str, subject: str, html_body: str) -> EmailMessage:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = recipient
        msg.add_alternative(html_body, subtype='html')
        return msg

    def build(self, survey: SurveyResult, subject: str = "") -> EmailMessage:
        if not subject:
            subject = self.subject

        html_body = self._insert_to_html(survey)
        recipient = survey.recipient_email
        return self._build_html_message(recipient, subject, html_body)
        

def main():
    template_path = os.path.join(
        os.path.dirname(os.path.abspath(__name__)),
        "email_templates",
        "email_template.html")
    
    with open(template_path, "r") as fin:
        html_template = fin.read()
    
    subject = "Projekt EASE - din egen strategi"

    email_user = os.environ.get('EMAIL_USER')
    email_pass = os.environ.get('EMAIL_PASS')
    builder = HTMLSurveyEmailBuilder(
        email_user, html_template, subject)

    sender = EmailSender(
        email_user, email_pass, 'smtp.aau.dk')

    survey = SurveyResult(0, 3, 
        "stuff123@build.eex",
        situations=("S1", "S2", "S3"),
        responses=("R1", "R2", "R3")
    )

    msg = builder.build(survey)
    sender.send(msg, debug_mode=False)


if __name__ == "__main__":
    main()
    
