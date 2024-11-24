import smtplib
from email.message import EmailMessage
import os

PASSWORD = os.getenv("EMAIL_PASSWORD", "your_password_here")
SENDER = os.getenv("EMAIL_SENDER", "your_email_here@gmail.com")
RECEIVER = os.getenv("EMAIL_RECEIVER", "receiver_email_here@gmail.com")

def send_email(image_path):
    message = EmailMessage()
    message["Subject"] = "Intruder Detected!"
    message.set_content("Hey, your webcam just detected an object.")

    with open(image_path, "rb") as image:
        image_content = image.read()

    message.add_attachment(image_content, maintype="image", subtype="jpg", filename=image_path)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email("images/4.jpg")
