import smtplib, ssl, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def mail_report(mail_to: str, data: str, subject: str = "Temat") -> bool:
    # dane do konfiguracji serwera poczty
    ip = "mail.abixedukacja.eu"
    port = 465  # For SSL
    login = "radom@abixedukacja.eu"
    password = "xxxxxxxxxxxxxx"
    mail_from = "radom@abixedukacja.eu"
    #

    text_type = 'plain'  # or 'html'
    msg = MIMEText(data, text_type, 'utf-8')

    msg['Subject'] = subject
    msg['From'] = mail_from
    #
    msg['To'] = mail_to

    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(ip, port, context=context) as server:
            server.login(login, password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
        return (True, "Test mail SUCCESS")
    except Exception as e:
        return (False, e)


if __name__ == "__main__":
    mail_to = "adam.jurkiewicz.pythonista@gmail.com"
    subject = "Tu wypełnij swój temat"
    msg_data = "Tu będzie treść maila."
    print(f"{mail_to=} {subject=}")
    mail_ok, report = mail_report(mail_to, msg_data, subject)
    if not mail_ok:
        print(f"Test mail failed - {report}")

