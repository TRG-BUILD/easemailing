import os
import unittest
from unittest.mock import patch, call
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
    return msg


class TestEmailSender(unittest.TestCase):
    user = "sender@mail.com"
    password = "123"
    tls_server = "myserver.mail.com"
    tls_port = 587
    debug_server = 'localhost'
    debug_port = 1025

    def test_exception_on_incorect_message(self):
        message = {"from": "A", "to": "B"}
        messages = [message]
        es = EmailSender(self.user, self.password, self.tls_server)
        self.assertRaises(Exception, es.send, messages, debug_mode=False)

    def test_exception_on_send_to_inactive_debug_server(self):
        message = create_email(self.user, "a@mail.com")
        es = EmailSender(self.user, self.password, self.tls_server)
        self.assertRaises(Exception, es.send, message, debug_mode=True)

    @patch('smtplib.SMTP')
    def test_can_send_one_email_to_debug_server(self, mock_smtp):
        message = create_email(self.user, "a@mail.com")
        messages = [message]
        es = EmailSender(self.user, self.password, self.tls_server, debug_port=self.debug_port)
        es.send(messages, debug_mode=True)

        # context manager
        context = mock_smtp.return_value.__enter__.return_value

        # correct connection
        mock_smtp.assert_called_once_with(self.debug_server, self.debug_port)

        # correct messaging
        context.send_message.assert_called_with(message)
        self.assertEqual(context.send_message.call_count, 1)

    @patch('smtplib.SMTP')
    def test_can_send_one_email_to_tls_server(self, mock_smtp):
        message = create_email(self.user, "a@mail.com")
        messages = [message]
        es = EmailSender(self.user, self.password, self.tls_server, self.tls_port)
        es.send(messages, debug_mode=False)

        # context manager
        context = mock_smtp.return_value.__enter__.return_value

        # correct connection
        mock_smtp.assert_called_once_with(self.tls_server, self.tls_port)
        self.assertEqual(context.ehlo.call_count, 2)
        context.starttls.assert_called()

        # correct login
        context.login.assert_called_once_with(self.user, self.password)

        # correct messaging
        context.send_message.assert_called_with(message)
        self.assertEqual(context.send_message.call_count, 1)

    @patch('smtplib.SMTP')
    def test_can_send_list_of_emails_to_tls_server(self, mock_smtp):
        message1 = create_email(self.user, "a@mail.com")
        message2 = create_email(self.user, "b@mail.com")
        messages = [message1, message2]
        es = EmailSender(self.user, self.password, self.tls_server, self.tls_port)
        es.send(messages, debug_mode=False)

        context = mock_smtp.return_value.__enter__.return_value

        # sent correct data
        self.assertEqual(context.send_message.call_count, 2)
        self.assertListEqual(
            context.send_message.call_args_list, [call(message1), call(message2)])
        
