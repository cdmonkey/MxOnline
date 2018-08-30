__author__ = 'cdmonkey'
__date__ = '2018/8/3 15:20'

import xadmin

from .models import *


class CourseAdmin:
    list_display = ["name", "desc", "degree", "student_num", "image", "add_time"]
    search_fields = ["name", "desc", "degree"]
    list_filter = ["name", "desc", "degree", "add_time"]


class LessonAdmin:
    list_display = ["course", "name", "add_time"]
    search_fields = ["course", "name"]
    list_filter = ["course__name", "name", "add_time"]


class VideoAdmin:
    list_display = ["lesson", "name", "add_time"]
    search_fields = ["lesson", "name"]
    list_filter = ["lesson", "name", "add_time"]


class CourseRecourseAdmin:
    list_display = ["course", "name", "download", "add_time"]
    search_fields = ["course", "name", "download"]
    list_filter = ["course", "name", "download", "add_time"]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseRecourse, CourseRecourseAdmin)

