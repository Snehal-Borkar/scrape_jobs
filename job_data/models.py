from django.db import models

# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=150)
    company=models.CharField(max_length=150)
    type=models.CharField(max_length=150)
    validity=models.CharField(max_length=150)


class Interest_url(models.Model):
    url=models.CharField(max_length=150)



class Non_Interest_url(models.Model):
    url=models.CharField(max_length=150)