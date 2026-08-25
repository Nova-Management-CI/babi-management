from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi.templating import Jinja2Templates
from app.core import settings
from ..base import BaseNotificationService

class EmailProvider(BaseNotificationService):
    def __init__(self):
        self.conf = ConnectionConfig(
            MAIL_USERNAME=settings.MAIL_USERNAME,
            MAIL_PASSWORD=settings.MAIL_PASSWORD,
            MAIL_FROM=settings.MAIL_FROM,
            MAIL_PORT=settings.MAIL_PORT,
            MAIL_SERVER=settings.MAIL_SERVER,
            MAIL_STARTTLS=False,
            MAIL_SSL_TLS=True,
            USE_CREDENTIALS=True,
        )
        self.fm = FastMail(self.conf)
        self.templates = Jinja2Templates(directory="templates")

    async def send(self, recipient: str, message: str, **kwargs):
        msg = MessageSchema(
            subject=kwargs.get("subject", "Notification Nova School"),
            recipients=[recipient],
            body=message,
            subtype=MessageType.plain
        )
        await self.fm.send_message(msg)

    async def send_code(self, email: str, code: str):
        html_content = self.templates.get_template("email_code.html").render(code=code)
        message = MessageSchema(
            subject="Code de validation Nova School",
            recipients=[email],
            body=html_content,
            subtype=MessageType.html
        )
        await self.fm.send_message(message)