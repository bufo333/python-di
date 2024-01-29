from abc import ABC, abstractmethod


class IEmailService(ABC):
    @abstractmethod
    def send_email(self, message: str) -> None:
        pass


class SMTPEmailService(IEmailService):
    def send_email(self, message: str) -> None:
        print(f"Sending email via SMTP: {message}")


class SendGridEmailService(IEmailService):
    def send_email(self, message: str) -> None:
        print(f"Sending email via SendGrid: {message}")


class MockEmailService(IEmailService):
    def send_email(self, message: str) -> None:
        print(f"Mock email (not sent): {message}")


class Mailer:
    def __init__(self, email_service: IEmailService):
        self.email_service = email_service

    def send_message(self, message: str) -> None:
        self.email_service.send_email(message)


class ServiceLocator:
    services = {
        "SMTP": SMTPEmailService(),
        "SendGrid": SendGridEmailService(),
        "Mock": MockEmailService()
    }

    @staticmethod
    def get_email_service(service_type: str) -> IEmailService:
        return ServiceLocator.services.get(service_type, MockEmailService())


service_type = "SendGrid"  # Conditionally determined
email_service = ServiceLocator.get_email_service(service_type)

mailer = Mailer(email_service)
mailer.send_message("Message for the selected service.")



# Alternate factory method

class EmailServiceFactory:
    def get_email_service(self, service_type: str) -> IEmailService:
        if service_type == "SMTP":
            return SMTPEmailService()
        elif service_type == "SendGrid":
            return SendGridEmailService()
        else:
            return MockEmailService()

service_type = "SMTP"  # This could be determined at runtime based on various factors
factory = EmailServiceFactory()
email_service = factory.get_email_service(service_type)

mailer = Mailer(email_service)
mailer.send_message("This is a message sent using the chosen service.")
