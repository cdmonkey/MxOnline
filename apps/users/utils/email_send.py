__author__ = 'cdmonkey'
__date__ = '2018/8/9 17:22'

from random import Random

from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from MxOnline.settings import DEFAULT_FROM_EMAIL


def get_random_str(random_length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) -1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0 ,length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = get_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "慕学在线网注册激活"
        email_body = "请点击下面的链接激活账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_res = send_mail(email_title, email_body,
                             DEFAULT_FROM_EMAIL, [email], fail_silently=False)
        if send_res:
            return True

    elif send_type == "forget":
        email_title = "慕学在线网密码重置"
        email_body = "请点击下面的链接密码重置：http://127.0.0.1:8000/reset/{0}".format(code)
        send_res = send_mail(email_title, email_body,
                             DEFAULT_FROM_EMAIL, [email], fail_silently=False)
        if send_res:
            return True

