import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
_user = ""
_pwd  = ""
_to   = ""
msg = MIMEMultipart()
msg["Subject"] = "电子发票申请"
msg["From"]    = _user
msg["To"]      = _to
part = MIMEText("这是文字部分")
msg.attach(part)
#---这是附件部分---
for name in os.listdir():
    if "." in name and "邮件发送" not in name:
        part = MIMEApplication(open(name,'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=name)
        msg.attach(part)
s = smtplib.SMTP("smtp.163.com", timeout=30)
s.login(_user, _pwd)
s.sendmail(_user, _to, msg.as_string())
s.close()
