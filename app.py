from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "1"
app.config.update(
    # 发送邮件的SMTP服务器
    MAIL_DEBUG = True,
    MAIL_SERVER = 'smtp.qq.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='1070649959@qq.com',  # 自己的邮箱
    MAIL_PASSWORD='qflnuszgautkbfhb',  # 邮箱密码
    MAIL_DEFAULT_SENDER=('1070649959@qq.com')  # 发送人，邮箱账号
)


mail = Mail(app)
@app.route('/')
def index():
    msg = Message(subject='Hello World',
                      recipients=['18336185670@163.com'])
    msg.body = 'sended by flask-email'
    # msg.html = '<b>测试Flask发送邮件<b>'
    mail.send(msg)
    return '<h1>邮件发送成功</h1>'

if __name__ == '__main__':
    app.run()

