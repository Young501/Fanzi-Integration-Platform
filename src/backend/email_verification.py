import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

class EmailVerification:
    def __init__(self):
        self.verification_codes = {}
        self.allowed_emails = ["530933620@qq.com", "3296937370@qq.com", "yangzechenau@gmail.com"]  # 允许发送验证码的邮箱

    def send_verification_code(self, email):
        if email not in self.allowed_emails:
            return "Email not authorized to receive verification code."

        #code = "123456"
        code = str(random.randint(100000, 999999))  # 生成6位验证码
        self.verification_codes[email] = code


        # 邮箱配置
        sender_email = "3296937370@qq.com"
        sender_password = "lqbspbocrkkbdagi"  # 使用授权码
        smtp_server = "smtp.qq.com"
        smtp_port = 587  # 使用TLS加密端口

        # 邮件内容
        subject = "Your Verification Code"
        body = f"Your verification code is: {code}"

        # 创建邮件
        message = MIMEText(body, 'plain', 'utf-8')
        message['From'] = formataddr(("Young", sender_email))   # 显示昵称+邮箱地址
        message['To'] = formataddr(("Receiver", email))
        message['Subject'] = Header(subject, 'utf-8')

        # 发送邮件
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # 启用TLS加密
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [email], message.as_string())
            server.quit()
            return "Verification code sent successfully."
        except smtplib.SMTPException as e:
            return f"SMTP error occurred: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def verify_code(self, email, code):
        return self.verification_codes.get(email) == code
