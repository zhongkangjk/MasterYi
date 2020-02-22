import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os,datetime
_user = "---"
_pwd  = "---"
_to   = "---"
today = datetime.date.today().strftime('%y%m%d')
msg = MIMEMultipart()
msg["Subject"] = today+'数据库备份'
msg["From"]    = _user
msg["To"]      = _to
part = MIMEText('这是'+ today + '份的数据文件')
msg.attach(part)
#---这是附件部分---
for name in os.listdir():
    if "db.sqlite3" in name :
        part = MIMEApplication(open(name,'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=today+'.sqlite3')
        msg.attach(part)
        break
s = smtplib.SMTP("smtp.qq.com", timeout=60)
try:
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.close()
    print("发送成功")
except:
    print("发送失败")
