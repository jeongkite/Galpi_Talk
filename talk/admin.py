from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'address_num', 'c_progress', 'q_progress']
    list_display_links = ['id', 'code']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'chap_num', 'content']
    list_display_links = ['id', 'chap_num', 'content']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter', 'content', 'limit', 'q_type']
    list_display_links = ['id', 'chapter', 'content']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter', 'question', 'content']
    list_display_links = ['id', 'chapter', 'content']


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'chapter', 'question', 'content']
    list_display_links = ['id', 'chapter', 'question', 'content']
    search_fields = ['code__access_code']
