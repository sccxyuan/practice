#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models
import datetime

class Article(models.Model):
    num=models.IntegerField(blank=False)
    name=models.CharField(max_length=30)
    img=models.ImageField('Image',upload_to='indeximages')
    node=models.TextField(blank=True)
    hoter=models.IntegerField(blank=True)

    
class Shop(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField('Image',upload_to='indeximages')
    node=models.TextField(blank=True)
    hoter=models.IntegerField(blank=True)

    
class New(models.Model):
    name=models.CharField(max_length=30,blank=False)
    writer=models.CharField(max_length=30)
    wtime=models.DateTimeField(default=datetime.datetime.now())
    content=models.TextField()
    hoter=models.IntegerField(blank=True)

    
class Message(models.Model):
    sub=models.CharField(max_length=25)
    content=models.TextField(blank=False)
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=20)
    email=models.EmailField(blank=True,verbose_name='e-mail')

    
# Create your models here.
