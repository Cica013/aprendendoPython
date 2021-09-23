from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'tunicodanado174@gmail.com'
minha_senha = 'Tunicodanado10#'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Silvanis Rodrigues', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Silvanis Rodrigues'
msg['to'] = meu_email
msg['subject'] = 'Este é um e-mail de teste. (Programando em Python)'
corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('GatoGalatico.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro: ', e)

