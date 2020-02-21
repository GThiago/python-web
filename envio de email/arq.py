from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib 

#141577-2.jpg

email = 'email aq'
senha = 'senha aq'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')

    corpo_msg = template.substitute(nome = 'Gabriel', data = data)

msg = MIMEMultipart()
msg['from'] = 'Gabriel'
msg['to'] = 'email envio'
msg['subject'] = 'Irmao so abre'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

'''with open('141577-2.jpg','rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)
'''

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, senha)
        smtp.send_message(msg)

        print(f'Email enviado para {msg["to"]}!')
    except Exception as e:
        print('Email nao enviado!')
        print('Erro:', e)
