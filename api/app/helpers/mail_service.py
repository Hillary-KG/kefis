from datetime import datetime
from threading import Thread
from flask_mail import Message
from api import mail
from flask import current_app


class MailService:
    def send_async_mail(self, message):
        with current_app.app_context():
            try:
                mail.send(message)
            except ConnectionRefusedError as e:
                # raise InternalServerError()
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[MAIL SERVER] not working")

    def send_email(self,subject, sender, recipients, text_body, html_body):
        msg = Message(subject, sender=sender, recipients=recipients)
        msg.body = text_body
        msg.html = html_body
        Thread(target=self.send_async_mail, args=(msg,)).start()
    
    
