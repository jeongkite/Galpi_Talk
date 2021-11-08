from accounts.models import AccessCode
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Info(models.Model):
    code = models.ForeignKey(
        AccessCode, on_delete=models.CASCADE, verbose_name="시리얼키")
    address_num = models.IntegerField(verbose_name="주소 개수")
    c_progress = models.IntegerField(verbose_name="챕터 진행")
    q_progress = models.IntegerField(verbose_name="질문 진행")


class Chapter(models.Model):
    chap_num = models.IntegerField(verbose_name="챕터 번호")
    content = models.TextField(verbose_name="보조내용", null=True, blank=True)


class Question(models.Model):
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, verbose_name="해당 챕터")
    content = models.TextField(verbose_name="질문 내용")
    limit = models.IntegerField(verbose_name="글자수")
    q_type = models.IntegerField(verbose_name="질문 타입")  # 0:주관, 1:객관


class Choice(models.Model):
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, verbose_name="해당 챕터")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="해당 질문")
    # 이미지인 경우 해당 파일명으로 처리 (ex. 12_1.jpg)
    content = models.TextField(verbose_name="선택지")


class Response(models.Model):
    code = models.ForeignKey(
        AccessCode, on_delete=models.CASCADE, verbose_name="시리얼키")
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, verbose_name="해당 챕터")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="해당 질문")
    content = models.CharField(max_length=900, verbose_name="")
