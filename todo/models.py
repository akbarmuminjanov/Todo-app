from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} of {self.user.username}"
    

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ["-datetime"]

    def __str__(self):
        return f" Todo of {self.user.username}"
    