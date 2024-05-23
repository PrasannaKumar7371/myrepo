from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    tittle = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=256)
    email = models.EmailField(max_length=30)
    phonenumber = models.BigIntegerField()
class VizagJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    tittle = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=256)
    email = models.EmailField(max_length=30)
    phonenumber = models.BigIntegerField()
class BngJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    tittle = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=256)
    email = models.EmailField(max_length=30)
    phonenumber = models.BigIntegerField()
