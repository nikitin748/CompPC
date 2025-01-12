from django.db import models

class NV(models.Model):
    model = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'nv'  # Имя таблицы в базе данных

class RD(models.Model):
    model = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'rd'  # Имя таблицы в базе данных

class Rizen(models.Model):
    model = models.CharField(max_length=100)
    motherboard = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'rizen'  # Имя таблицы в базе данных

class Intel(models.Model):
    model = models.CharField(max_length=100)
    motherboard = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'intel'  # Имя таблицы в базе данных

class OtherSet(models.Model):
    cooler = models.CharField(max_length=100)
    RAM = models.CharField(max_length=100)
    bp = models.CharField(max_length=100)
    priceSum = models.IntegerField()

    class Meta:
        db_table = 'otherset'  # Имя таблицы в базе данных







