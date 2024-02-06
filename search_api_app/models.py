from django.db import models

class Data(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=255)
    creator=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    number=models.IntegerField()
    dispo=models.BooleanField()
    price=models.FloatField()