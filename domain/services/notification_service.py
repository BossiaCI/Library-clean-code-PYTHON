# domain/services/notification_service.py
class NotificationService:
    def send_email(self, email: str, message: str):
        # In a real application, integrate with an email provider.
        print(f"Sending email to {email}: {message}")

    def send_sms(self, phone_number: str, message: str):
        # In a real application, integrate with an SMS provider.
        print(f"Sending SMS to {phone_number}: {message}")
