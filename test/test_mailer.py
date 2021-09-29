import os
import unittest
from unittest.mock import patch
from email.message import EmailMessage

from easemail.mailer import EmailSender

def get_secret():
    """Simple retrieval function.
    Returns SECRET or raises OSError.
    """
    secret = os.getenv('SECRET', default=None)

    if secret is None:
        raise OSError("SECRET environment is not set.")

    return secret

def create_email(sender: str, reciever: str):
    msg = EmailMessage()
    msg['Subject'] = 'mailing_test'
    msg['From'] = sender
    msg['To'] = reciever
    msg.set_content('mailing_test')


class TestEmailSender(unittest.TestCase):
    user=  "sender@mail.com"
    password = "123"
    server = "myserver.mail.com"

    def test_works_with_emailmessage(self):
        message = {"from": "A", "to": "B"}
        messages = [message]

        es = EmailSender(
            user="",
            password="",
            server=""
        )
        self.assertRaises(Exception, es.send, messages, debug_mode=True)

    def test_raises_on_send_to_inactive_debug_server(self):
        message = create_email(sender="test")

        es = EmailSender(
            user="",
            password="",
            server=""
        )
        self.assertRaises(Exception, es.send, message, debug_mode=True)

    def test_can_send_one_email(self):
        message = create_email(self.user, "a@mail.com")
        messages = [message]

        with patch('smtplib.SMTP', autospec=True) as mock_smtp:
            es = EmailSender(self.user, self.password, self.server)
            es.send(messages, debug_mode=False)

            context = mock_smtp.return_value.__enter__.return_value
            self.assertEqual(context.ehlo.call_count, 2)
            context.starttls.assert_called()
            self.assertEqual(context.login.call_count, 1)
            context.send_message.assert_called_with(message)
            self.assertEqual(context.send_message.call_count, 1)

    def test_can_send_list_of_emails(self):
        message1 = create_email(self.user, "a@mail.com")
        message2 = create_email(self.user, "b@mail.com")
        messages = [message1, message2]

        with patch('smtplib.SMTP', autospec=True) as mock_smtp:

            es = EmailSender(self.user, self.password, self.server)
            es.send(messages, debug_mode=False)

            context = mock_smtp.return_value.__enter__.return_value

            
            # connected correctly
            self.assertEqual(context.ehlo.call_count, 2)
            context.starttls.assert_called()
            self.assertEqual(context.login.call_count, 1)

            # NOT TRUE!
            """
            self.assertEqual(context.login.called_with(
                user="test1@gmail.com",
                password=""),
                True
            )
            """

            # sent correct data
            context.send_message.assert_called_with(message1)
            context.send_message.assert_called_with(message2)
            self.assertEqual(context.send_message.call_count, 2)
