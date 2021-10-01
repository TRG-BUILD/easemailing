import os
from abc import ABC, abstractmethod
from email.message import EmailMessage
from string import Template

from bs4 import BeautifulSoup
from easemail.datasets import SurveyResult

class SurveyEmailBuilder(ABC):
    """
    builder for EmailMessage objects
    """
    def __init__(self, sender: str, subject: str=""):
        self.sender = sender
        self.subject = subject

    @abstractmethod
    def build(self, survey: SurveyResult, subject: str = "") -> EmailMessage:
        """
        build an email from SurveyResult
        """


class TextSurveyEmailBuilder(SurveyEmailBuilder):
    def __init__(self, text_template: str, sender: str, subject: str = ""):
        super().__init__(sender, subject)
        self.text_template = Template(text_template)

    def _insert_to_text(self, survey: SurveyResult) -> str:
        """
        Find text template tags present in data and substitute them with data
        """
        data = survey.get_dict()
        return self.text_template.safe_substitute(**data)

    def _build_text_message(self, recipient: str, subject: str, body: str) -> EmailMessage:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = recipient
        msg.set_content(body)
        return msg

    def build(self, survey: SurveyResult, subject: str = "") -> EmailMessage:
        if not subject:
            subject = self.subject

        body = self._insert_to_text(survey)
        recipient = survey.recipient_email
        return self._build_text_message(recipient, subject, body)


class HTMLSurveyEmailBuilder(SurveyEmailBuilder):
    def __init__(self, html_template: str, sender: str, subject: str = ""):
        super().__init__(sender, subject)
        self.html_template = html_template

    def _insert_to_html(self, survey: SurveyResult) -> str:
        """
        Find html template ids present in data and substitute them with data
        """
        data = survey.get_dict()

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