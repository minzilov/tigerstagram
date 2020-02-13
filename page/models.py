from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #밖에있는DB를참조할수있음
    pub_date = models.DateTimeField('publish') #작성일자
    content = models.TextField()


    def __str__(self):
        return self.title