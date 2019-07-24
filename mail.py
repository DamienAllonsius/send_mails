""" Mail file
Sends automatically a mail

Usage:
    mail <from_address> <password> <target_address> <subject> <content>

where
    <from_address> your gmail address
    <password> is the password of your gmail account
    <target_address> your target email address
    <subject> is the email subject
    <content> is the email content
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__)
    
    msg = MIMEMultipart()
    msg['From'] = args['<from_address>']
    msg['To'] = args['<target_address>']
    msg['Subject'] = args['<subject>']
    message = args['<content>']
    
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(args['<from_address>'], args['<password>'])
    mailserver.sendmail(args['<from_address>'], args['<target_address>'], msg.as_string())
    mailserver.quit()
