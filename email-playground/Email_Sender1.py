import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import path

html = Template(path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Amit Singh'
email['to'] = 'mailmeami27@gmail.com'
email['subject'] = 'you won 10 rupees'

email.set_content(html.substitute({'name': 'TinTinn'}). 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('amitksingh742@gmail.com', '1.Billion')
	smtp.send_message(email)
	print('all good!')