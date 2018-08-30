"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings

from users import views as users_view
from organization import views as org_view

import xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('index.html', TemplateView.as_view(template_name="index.html"), name="index"),
    path('login/', users_view.LoginView.as_view(), name="login"),
    # path('logout/', TemplateView.as_view(template_name="login.html"), name="logout"),
    path('register/', users_view.RegisterView.as_view(), name="register"),
    path('captcha/', include('captcha.urls')),
    path('active/<active_code>', users_view.ActiveView.as_view()),
    path('forget/', users_view.ForgetPwdView.as_view(), name="forget_pwd"),
    path('reset/<reset_code>', users_view.ResetPwdView.as_view(), name="reset_pwd"),
    path('modify/', users_view.ModifyPwdView.as_view(), name="modify_pwd"),
    # 课程机构首页
    path('org-list.html', org_view.OrgListView.as_view(), name="org_list"),
    # Media
    path('media/<path:path>', serve, {"document_root": settings.MEDIA_ROOT}),
]

# + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
