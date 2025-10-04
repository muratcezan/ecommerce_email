# email/email.py

from flask import current_app
from flask_mail import Mail, Message

# Tek bir Mail örneği oluşturup uygulama başlatılırken init_app ile bağlayacağız
mail = Mail()

def init_mail(app):
    """
    Uygulama başlatılırken çağırın:
        from admin_app.utils.email import init_mail
        init_mail(app)
    Bu sayede config'teki MAIL_... ayarlarını okuyarak Mail uzantısını kaydeder.
    """
    mail.init_app(app)

def send_email(to: str, subject: str, body: str, html: str = None) -> None:
    """
    Tek bir alıcıya e-posta gönderir.

    Args:
        to: Alıcının e-posta adresi
        subject: E-posta konusu
        body: Düz metin (plain-text) mesaj gövdesi
        html: (Opsiyonel) HTML gövdesi

    Config Gereksinimleri (app.config):
        MAIL_SERVER
        MAIL_PORT
        MAIL_USE_TLS veya MAIL_USE_SSL
        MAIL_USERNAME
        MAIL_PASSWORD
        MAIL_DEFAULT_SENDER
    """
    msg = Message(
        subject=subject,
        recipients=[to],
        body=body,
        html=html,
        sender=current_app.config.get('MAIL_DEFAULT_SENDER')
    )
    mail.send(msg)
