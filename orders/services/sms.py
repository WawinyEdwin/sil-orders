import africastalking

from core import settings


class SmsService:
    def __init__(self):
        username = settings.AT_USERNAME
        api_key = settings.AT_API_KEY
        africastalking.initialize(username, api_key)
        self.sms = africastalking.SMS

    def send(self, phone, message):
        try:
            response = self.sms.send(message, [phone])
            if response["SMSMessageData"]["Recipients"][0]["status"] == "Success":
                return True
            else:
                return False
        except Exception as e:
            # Log or handle the exception properly
            print("Failed to send SMS:", e)
            return False
