from django.db import models

# Create your models here.


class AccessCode(models.Model):
    access_code = models.CharField(max_length=100)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.access_code
