from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=30)
    id=models.CharField(primary_key=True,max_length=30)
    latitude=models.CharField(max_length=40)
    longitude=models.CharField(max_length=40)

    def __str__(self):
        return self.name
