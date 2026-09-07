import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "proposal for vinayaka chavithi"
msg["From"] = "angerideepika@gmail.com"
msg["To"] = "sreeteja135@gmail.com"

msg.set_content("""
Dear buchey,

Greetings from Deepika..

Welcome to poch mummy festival and Ganesh festival.

Best regards,
DEEPika
""")

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("angerideepika@gmail.com", "efrtxctirxpcuihg")

server.send_message(msg)

print("Email sent successfully")

server.quit()