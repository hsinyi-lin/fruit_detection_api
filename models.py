# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    password = models.TextField()
    nickname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'account'


class Answer(models.Model):
    question = models.ForeignKey('Question', models.DO_NOTHING)
    email = models.ForeignKey(Account, models.DO_NOTHING, db_column='email')
    content = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'answer'


class Fruit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    nutrition = models.CharField(max_length=45, blank=True, null=True)
    prevent = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fruit'


class Question(models.Model):
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=100)
    email = models.ForeignKey(Account, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'question'


class Recipe(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    step = models.TextField(blank=True, null=True)
    ingredient = models.CharField(max_length=100, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'
