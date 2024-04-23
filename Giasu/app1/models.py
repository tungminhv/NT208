from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TUTOR(models.Model):
    name = models.CharField(max_length=50, null=False)
    subject = models.CharField(max_length=50, null=False)
    Optimistic = models.IntegerField(default=0, null=True, blank=True)
    Introduction = models.CharField(max_length=300, null=False)
    Proficiency = models.CharField(max_length=200, null=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url