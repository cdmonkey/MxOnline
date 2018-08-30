__author__ = 'cdmonkey'
__date__ = '2018/8/3 13:32'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = "hehe"
    site_footer = "cdmonkey"
    menu_style = "accordion"


class EmailVerifyRecordAdmin:
    list_display = ["code", "email", "send_type", "send_time"]
    search_fields = ["code", "email", "send_type"]
    list_filter = ["code", "email", "send_type"]


class BannerAdmin:
    list_display = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "image"]
    list_filter = ["title", "image", "index", "add_time"]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

