from abc import ABC, abstractmethod

class EmailClient(ABC):
    @abstractmethod
    def send_mail(self, to, subject, body):
        pass


class GmailClientImpl(EmailClient):
    def send_mail(self, to, subject, body):
        print("Connecting to GMAIL SMTP Server...")
        print(f"Sending email via GMAIL to : {to}")
        print("Sent Email Successfully")


class OutlookClientImpl(EmailClient):
    def send_mail(self, to, subject, body):
        print("Sending mail via Outlook")



class EmailService:
    def __init__(self, email_client: EmailClient):
        self.email_client = email_client

    def send_welcome_email(self, user_email, user_name):
        subject = f"Welcome {user_name}!"
        body = "thanks for signingup"
        self.email_client.send_mail(user_email, subject, body)


if __name__ == "__main__":
    gmail = EmailService(GmailClientImpl())
    gmail.send_welcome_email("nitin@gmail.com", "nitin")

    #outlook
    print("\n Using Outlook ")
    outlook = EmailService(OutlookClientImpl())
    outlook.send_welcome_email("nitish@gmail.com", "nitish")


