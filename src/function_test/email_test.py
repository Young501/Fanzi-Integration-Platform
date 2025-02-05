import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr 

# 邮箱配置
sender_email = "3296937370@qq.com"
sender_password = "lqbspbocrkkbdagi"  # 使用获取的授权码
smtp_server = "smtp.qq.com"
smtp_port = 587  # 使用TLS加密端口

# 邮件内容
receiver_email = "yangzechenau@gmail.com"
subject = "测试邮件"
body = "这是一封来自Python的测试邮件。"


# 创建邮件
message = MIMEText(body, 'plain', 'utf-8')

# 正确设置From和To字段
message['From'] = formataddr(("Young", sender_email))  # 显示昵称+邮箱地址
message['To'] = formataddr(("Receiver", receiver_email))
message['Subject'] = Header(subject, 'utf-8')

# 发送邮件
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # 启用TLS加密
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, [receiver_email], message.as_string())
    print("邮件发送成功！")
    server.quit()
except Exception as e:
    print(f"邮件发送失败: {e}")
