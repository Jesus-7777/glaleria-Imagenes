from smtplib import SMTP
from email.message import EmailMessage
from config import settings



message = EmailMessage()

message['Subjet'] = 'Este es el asunto'
message['From'] = 'dubanruales2020@itp.edu.co'
message['To'] = 'duvanruales99@gmail.com'
message.set_content('Este es un Email de pruebas')

username = settings.SMPT_USERNAME
password = settings.SMPT_PASSWORD
print(username,password,settings.SMPT_HOSTNAME)
server=SMTP(settings.SMPT_HOSTNAME)
server.starttls()
server.login(username, password)
server.send_message(message)

server.quit()

