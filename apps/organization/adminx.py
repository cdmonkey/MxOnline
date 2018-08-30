__author__ = 'cdmonkey'
__date__ = '2018/8/3 15:58'


import xadmin

from .models import City, CourseOrg, Teacher


class CityAdmin:
    list_display = ["name", "desc", "add_time"]
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "add_time"]


class CourseOrgAdmin:
    list_display = ["name", "desc", "category", "image", "address", "city", "add_time"]
    search_fields = ["name", "desc", "category", "address", "city"]
    list_filter = ["name", "desc", "category", "image", "address", "city", "add_time"]


class TeacherAdmin:
    list_display = ["name", "org", "work_years", "work_company", "work_position", "points", "add_time"]
    search_fields = ["name", "org", "work_years", "work_company", "work_position", "points"]
    list_filter = ["name", "org", "work_years", "work_company", "work_position", "points", "add_time"]


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
