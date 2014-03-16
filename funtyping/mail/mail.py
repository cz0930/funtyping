#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
from email.mime.image import MIMEImage

def mailregist(tomail):
    fromaddr = ''
    toaddrs  = [tomail]

    msg = MIMEMultipart()
    msg['Subject'] = '这是一封测试邮件PYthon'
    msg['From'] = fromaddr
    msg['To'] = ";".join(toaddrs)
    
    with open('/root/pytest/day3/funtyping/funtyping/mail/regist_mail.tpl', 'r') as fd:
        data = fd.read()

    txt = MIMEText(data,_subtype='html') 
    msg.attach(txt) 

    BAK_DIR = '/root/pytest/mail/mt/'

    for fileName in os.listdir(BAK_DIR):

        ctype, encoding = mimetypes.guess_type(fileName)  
        if ctype is None or encoding is not None:  
            ctype = 'application/octet-stream' 
        maintype, subtype = ctype.split('/', 1)  
        att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(os.path.join(BAK_DIR, fileName), 'rb'))[0], _subtype = subtype)  
        att1.add_header('Content-Disposition', 'attachment', filename = fileName)  
        msg.attach(att1)  

    username = ''
    password = ''

    server = smtplib.SMTP('')
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()
    return ''


