import smtplib
from typing import List
from email.message import EmailMessage


class MailingError(Exception):
    pass


class EmailSender:
    def __init__(self, user: str, password: str, server:str, tls_port: int=587, debug_port: int=1025):
        self.user = user
        self.password = password
        self.server = server
        self.tls_port = tls_port
        self.debug_port = debug_port

    def _send_tls(self, messages: List[EmailMessage]) -> bool:
        """
        Sends a list of EmailMessage objects via TLS
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
        Sends a list of emails to localhost SMTP DebuggingServer for local testing
        start server with:
        python -m smtpd -c DebuggingServer -n localhost:1025 
        """
        try:
            with smtplib.SMTP('localhost', self.debug_port) as smtp:
                for m in messages:
                    smtp.send_message(m)
        except:
            raise MailingError("Cannot send localhost email")

    def send(self, messages: List[EmailMessage], debug_mode=False):
        """
        Sends a list of emails in either TLS mode ore debug
        """
        if not isinstance(messages, list):
            raise ValueError("Expected list of email.message.EmailMessage")

        if debug_mode:
            self._send_debug(messages)
        else:
            self._send_tls(messages)



def main():
    pass


if __name__ == "__main__":
    main()
    
