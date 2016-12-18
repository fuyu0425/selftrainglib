from django.db import models


# Create your models here.


class Gallery(models.Model):
    title = models.CharField('title', max_length=100)
    serial = models.CharField('serial_number', unique=True, primary_key=True, max_length=100)
    cover = models.URLField('cover_url', blank=True, null=True)
    begin = models.DateField('begin_date')
    end = models.DateField('end_data')
    people = models.CharField('people', max_length=100)
    place = models.CharField('place', max_length=100)
    description = models.TextField('description')


class Item(models.Model):
    serial = models.ForeignKey('Gallery', related_name='items')
    title = models.CharField('image_name', max_length=100)
    imgPath = models.URLField('imgPath')
