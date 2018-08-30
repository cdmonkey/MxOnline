__author__ = 'cdmonkey'
__date__ = '2018/8/3 16:20'

import xadmin

from .models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourses


class UserAskAdmin:
    list_display = ["name", "mobile", "course_name", "add_time"]
    search_fields = ["name", "mobile", "course_name"]
    list_filter = ["name", "mobile", "course_name", "add_time"]


class CourseCommentAdmin:
    list_display = ["user", "course__name", "comments", "add_time"]
    search_fields = ["user", "course__name", "comments", "add_time"]
    list_filter = []


class UserFavoriteAdmin:
    list_display = ["user__name", "fav_id", "fav_type", "add_time"]
    search_fields = ["user__name", "fav_id", "fav_type"]
    list_filter = ["user__name", "fav_id", "fav_type", "add_time"]


class UserMessageAdmin:
    list_display = ["user", "message", "has_read", "send_time"]
    search_fields = ["user", "message", "has_read"]
    list_filter = ["user", "message", "has_read", "send_time"]


class UserCoursesAdmin:
    list_display = ["user__name", "course__name", "add_time"]
    search_fields = ["user__name", "course__name"]
    list_filter = ["user__name", "course__name", "add_time"]


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourses, UserCoursesAdmin)
