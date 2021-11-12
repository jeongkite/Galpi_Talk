from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AccessCode(models.Model):
    access_code = models.CharField(max_length=100)
    is_used = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="유저")

    def __str__(self):
        return self.access_code
# access_code[0] = A:0 -> 주소 입력 X, B:3, C:5


class Privacy(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="유저", null=True
    )

    name = models.CharField(max_length=10, verbose_name="이름")
    birth = models.CharField(max_length=8, verbose_name="생년월일")

    l_food1 = models.CharField(max_length=10, verbose_name="좋아하는 음식1")
    l_food2 = models.CharField(max_length=10, verbose_name="좋아하는 음식2")
    l_food3 = models.CharField(max_length=10, verbose_name="좋아하는 음식3")

    h_food1 = models.CharField(max_length=10, verbose_name="싫어하는 음식1")
    h_food2 = models.CharField(max_length=10, verbose_name="싫어하는 음식2")
    h_food3 = models.CharField(max_length=10, verbose_name="싫어하는 음식3")

    good = models.CharField(max_length=20, verbose_name="장점")
    bad = models.CharField(max_length=20, verbose_name="단점")
    hobby = models.CharField(max_length=20, verbose_name="취미")


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="유저", null=True
    )
    name = models.CharField(max_length=5, verbose_name="수령인")
    phone = models.CharField(max_length=11, verbose_name="전화번호")
    postal = models.CharField(max_length=5, verbose_name="우편번호")
    addy = models.CharField(max_length=100, verbose_name="주소")
    is_other = models.BooleanField(default=True, verbose_name="타인?")
