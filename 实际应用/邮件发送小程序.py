import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def 发送邮件(邮件标题,称呼,邮件文字,发件人邮箱,密码,收件人邮箱,附件路径列表,附件命名列表):
    msg = MIMEMultipart()
    msg["Subject"] = 邮件标题
    msg["From"]    = 发件人邮箱
    msg["To"]      = 称呼
    #这是文字部分
    part = MIMEText(邮件文字)
    msg.attach(part)
    #这是附件部分
    for 附件路径,附件命名 in zip(附件路径列表,附件命名列表):
        part = MIMEApplication(open(附件路径,'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=附件命名)
        msg.attach(part)

    s = smtplib.SMTP("smtp.qq.com", timeout=60)#SMTP服务的网址
    try:
        s.login(发件人邮箱, 密码)
        s.sendmail(发件人邮箱, 收件人邮箱, msg.as_string())#收件人邮箱可以是列表
        s.close()
        print("发送成功")
    except:
        print("发送失败")


