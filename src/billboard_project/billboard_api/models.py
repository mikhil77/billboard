from django.db import models


class UserProfile(models.Model):

    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/',blank=True,null=True)
    availabilty = models.BooleanField(default=True)

    def __str__(self):
        return self.name
