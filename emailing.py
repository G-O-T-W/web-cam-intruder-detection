import smtplib
from email.message import EmailMessage

PASSWORD = "onboooljmprmrzns"
SENDER = "rishavdiyali@gmail.com"
RECEIVER = "diyali.rishav.22@gmail.com"

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
