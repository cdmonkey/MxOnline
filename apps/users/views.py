from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.views.generic.base import View
from django.db.models import Q
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginFrom, RegisterForm, ForgetForm, ResetPwdForm

from .utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        login_form = LoginFrom()
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginFrom(request.POST)
        res = login_form.is_valid()
        if res:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html", {})
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        res = register_form.is_valid()
        if res:
            username = request.POST.get("email")
            user_is_exist = UserProfile.objects.get(email=username)
            if user_is_exist:
                return render(request, "register.html", {
                    "register_form": register_form,
                    "msg": "邮箱已被注册"})
            password = request.POST.get("password")
            new_user = UserProfile.objects.create()
            new_user.username = username
            new_user.email = username
            new_user.password = make_password(password)
            new_user.is_active = False
            new_user.save()

            send_res = send_register_email(new_user.email, "register")
            if send_res:
                return render(request, "login.html", {"register_form": register_form})
        else:
            return render(request, "register.html", {"register_form": register_form})


class ActiveView(View):
    def get(self, request, active_code):
        res = EmailVerifyRecord.objects.get(code=active_code)
        if res:
            email = res.email
            user = UserProfile.objects.get(email=email)
            if user.is_active:
                return HttpResponse("用户已激活，无需重复激活")
            else:
                user.is_active = True
                user.save()
                return HttpResponse("Success!")
        else:
            error_msg = "激活码错误"
            # return render(request, "register.html", {"error_msg": error_msg})
            return HttpResponse(error_msg)


class ForgetPwdView(View):
    def get(self, request):
        forgetpwd_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forgetpwd_form": forgetpwd_form})

    def post(self, request):
        forgetpwd_form = ForgetForm(request.POST)
        res = forgetpwd_form.is_valid()
        if res:
            email = request.POST.get("email")
            user_is_exist = UserProfile.objects.filter(username=email)
            if user_is_exist:
                send_res = send_register_email(email, "forget")
                if send_res:
                    return HttpResponse("Send mail success!")
            else:
                return render(request, "forgetpwd.html", {
                    "msg": "邮箱不存在", "forgetpwd_form": forgetpwd_form})
        else:
            return render(request, "forgetpwd.html", {"forgetpwd_form": forgetpwd_form})


class ResetPwdView(View):
    def get(self, request, reset_code):
        res = EmailVerifyRecord.objects.get(code=reset_code)
        if res:
            email = res.email
            return render(request, "password_reset.html", {"email": email})
        else:
            error_msg = "重置码错误"
            return HttpResponse(error_msg)


class ModifyPwdView(View):
    def post(self, request):
        resetpwd_form = ResetPwdForm(request.POST)
        res = resetpwd_form.is_valid()
        if res:
            email = request.POST.get("email")
            pwd1 = request.POST.get("password1")
            pwd2 = request.POST.get("password2")
            if pwd1 == pwd2:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd1)
                user.save()
                return render(request, "login.html", {})
            else:
                return render(request, "password_reset.html", {"msg": "密码不一致"})
        else:
            return render(request, "password_reset.html", {"resetpwd_form": resetpwd_form})



# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return render(request, "index.html", )
#         else:
#             return render(request, "login.html", {"msg": "用户名或密码错误"})
#
#     elif request.method == "GET":
#         return render(request, "login.html", {})
