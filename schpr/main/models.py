from django.db import models

class NV(models.Model):
    model = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'nv'

class RD(models.Model):
    model = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'rd'

class Rizen(models.Model):
    model = models.CharField(max_length=100)
    motherboard = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'rizen'

class Intel(models.Model):
    model = models.CharField(max_length=100)
    motherboard = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'intel'

class OtherSet(models.Model):
    cooler = models.CharField(max_length=100)
    RAM = models.CharField(max_length=100)
    bp = models.CharField(max_length=100)
    priceSum = models.IntegerField()

    class Meta:
        db_table = 'otherset'







