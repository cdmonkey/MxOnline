__author__ = 'cdmonkey'
__date__ = '2018/8/8 13:55'

from django import forms
from django.forms import fields
from captcha.fields import CaptchaField


class LoginFrom(forms.Form):
    username = fields.CharField(required=True)
    password = fields.CharField(required=True, min_length=3)


class RegisterForm(forms.Form):
    email = fields.EmailField(required=True)
    password = fields.CharField(required=True, min_length=3)
    captcha = CaptchaField()


class ForgetForm(forms.Form):
    email = fields.EmailField(required=True)
    captcha = CaptchaField()


class ResetPwdForm(forms.Form):
    email = fields.EmailField(required=True)
    password1 = fields.CharField(required=True, min_length=3)
    password2 = fields.CharField(required=True, min_length=3)
