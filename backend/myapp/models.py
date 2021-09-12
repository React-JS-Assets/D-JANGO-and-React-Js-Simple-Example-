
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.fields import EmailField
# Create your models here.


class user(AbstractUser):
    first_name = models.CharField(max_length=120)
    # username = models.CharField(max_length=120, unique=True)
    last_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    # EmailField = models.CharField(max_length=120)


class Todo(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
