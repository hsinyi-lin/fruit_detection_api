from django.db import models


class Account(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    password = models.TextField()
    nickname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'account'


class Fruit(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    content = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fruit'


class Recipe(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)
    step = models.CharField(max_length=45, blank=True, null=True)
    ingredient = models.CharField(max_length=45, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'
