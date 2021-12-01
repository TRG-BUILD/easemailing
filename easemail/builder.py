import os
from abc import ABC, abstractmethod
from email.message import EmailMessage
from string import Template

from bs4 import BeautifulSoup
from easemail.datasets import SurveyResult


class IncorrectTemplate(Exception):
    pass


class SurveyEmailBuilder(ABC):
    """
    builder for EmailMessage objects
    """

    def __init__(self, sender: str, subject: str = ""):
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
        try:
            return self.text_template.substitute(**data)
        except KeyError as e:
            raise IncorrectTemplate("Template has unused tags! ", e)

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
        found_keys = []
        for key, new_text in data.items():
            elem = soup.find(id=key)
            if elem:
                elem.string = new_text
                found_keys.append(key)

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
    path = os.path.join("email_templates", "email_template.html")
    if not os.path.exists(path):
        raise FileExistsError

    builder = HTMLSurveyEmailBuilder(
        open(path, "r").read(),
        "sender@mailcom",
        "from main"
    )

    s = SurveyResult(
        0, "recipient@mailcom", 0,
        situations=("s0", "s1", "s2"),
        responses=("r0", "r1", "r2")
    )
    txt = builder._insert_to_html(s)


if __name__ == "__main__":
    main()
