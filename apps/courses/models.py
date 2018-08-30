
from datetime import datetime

from django.db import models

# Create your models here.


class Course(models.Model):
    degree_choice = (
        ("chu", "初级"),
        ("zhong", "中级"),
        ("gao", "高级"),
    )
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(max_length=6, choices=degree_choice, verbose_name="难度")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟）")
    student_num = models.IntegerField(default=0, verbose_name="学习人数", null=True, blank=True)
    fav_num = models.IntegerField(default=0, verbose_name="收藏人数", null=True, blank=True)
    image = models.ImageField(max_length=100, upload_to="courses/%Y/%m", verbose_name="课程封面")
    click_num = models.IntegerField(default=0, verbose_name="点击量", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程章节视频"
        verbose_name_plural = verbose_name


class CourseRecourse(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="资源名")
    download = models.FileField(max_length=100, upload_to="courses/resource/%Y/%m", verbose_name="课程资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name
