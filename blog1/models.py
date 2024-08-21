from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length=100)
    author= models.ForeignKey(User,on_delete=models.CASCADE )
    body= models.TextField()
    def __str__(self):
        return self.title + '|' + str(self.author)