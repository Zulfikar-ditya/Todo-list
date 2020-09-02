from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    date_add = models.DateTimeField(auto_now=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.value

    def delete(self, **kwargs):
        self.status = False
        self.save()
