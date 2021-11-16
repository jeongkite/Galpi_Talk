from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address_num', 'c_progress', 'q_progress']
    list_display_links = ['id', 'user']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'chap_num', 'title', 'content']
    list_display_links = ['id', 'chap_num', 'content']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter', 'content', 'limit', 'q_type', 'star']
    list_display_links = ['id', 'chapter', 'content']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter', 'question', 'content']
    list_display_links = ['id', 'chapter', 'content']


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'chapter', 'question', 'content']
    list_display_links = ['id', 'chapter', 'question', 'content']
    search_fields = ['user__username', 'username']


@admin.register(LastHello)
class LastHelloAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'chapter', 'question', 'name', 'contact']
    list_display_links = ['id', 'chapter', 'question']
    search_fields = ['user_username']
