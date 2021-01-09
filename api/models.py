from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):

    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE ,blank=True ,null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + self.title