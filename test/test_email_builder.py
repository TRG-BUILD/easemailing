import os
import unittest
from email.message import EmailMessage

from easemail.datasets import SurveyResult
from easemail.builder import HTMLSurveyEmailBuilder, TextSurveyEmailBuilder, IncorrectTemplate


def build_html_message(sender: str, recipient: str, subject: str, body: str) -> EmailMessage:
    """
    Build text email message
    """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.add_alternative(body, subtype='html')
    return msg

def build_text_message(sender: str, recipient: str, subject: str, body: str) -> EmailMessage:
    """
    Build text email message
    """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content(body)
    return msg

def get_test_template(name: str):
    """
    Load test templates
    """
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "data",
        name
    )
    if os.path.exists(path):
        with open(path, "r") as fin:
            return fin.read()
    else:
        raise FileExistsError("File does not exist: ", path)


class TestTextSurveyEmailBuilder(unittest.TestCase):
    template_txt = get_test_template("template_text_email.txt")
    expected_txt = get_test_template("expected_text_email.txt")
    sender = "me@mail.com"
    recipient = "you@mail.com"
    subject = "testing pass!"

    def test_incomplete_insertion_raises(self):
        builder = TextSurveyEmailBuilder(
            self.template_txt,
            self.sender,
            self.subject
        )

        s = SurveyResult(
            0, self.recipient, 0,
            situations=("s0","s1"),
            responses=("r0",)
        )
        self.assertRaises(IncorrectTemplate, builder._insert_to_text, s)

    def test_correct_complete_insertion(self):
        builder = TextSurveyEmailBuilder(
            self.template_txt,
            self.sender,
            self.subject
        )

        s = SurveyResult(
            0, self.recipient, 0,
            situations=("s0", "s1", "s2"),
            responses=("r0", "r1", "r2")
        )
        txt = builder._insert_to_text(s)
        self.assertEqual(txt, self.expected_txt)

    def test_correct_complete_email(self):
        builder = TextSurveyEmailBuilder(
            self.template_txt,
            self.sender,
            self.subject
        )

        s = SurveyResult(
            0, self.recipient, 0,
            situations=("s0", "s1", "s2"),
            responses=("r0", "r1", "r2")
        )
        expected_mail = build_text_message(
            self.sender,
            self.recipient,
            self.subject,
            self.expected_txt
        )
        mail = builder.build(s)
        self.assertEqual(mail.as_string(), expected_mail.as_string())
        

class TestHTMLSurveyEmailBulder(unittest.TestCase):
    template_html = get_test_template("template_html_email.html")
    expected_html = get_test_template("expected_html_email.html")
    sender = "me@mail.com"
    recipient = "you@mail.com"
    subject = "testing pass!"

    def test_correct_complete_insertion(self):
        builder = HTMLSurveyEmailBuilder(
            self.template_html,
            self.sender,
            self.subject
        )

        s = SurveyResult(
            0, self.recipient, 0,
            situations=("s0", "s1", "s2"),
            responses=("r0", "r1", "r2")
        )
        html = builder._insert_to_html(s)
        self.maxDiff = None
        self.assertListEqual(
            [r.strip() for r in html.splitlines() if r],
            [r.strip() for r in self.expected_html.splitlines() if r]
        )
        

