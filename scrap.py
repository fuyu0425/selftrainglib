#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os, django
import sys
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lib.settings")

django.setup()
from api.models import *


def getgalleryurl(number):
    return 'http://hall.lib.nctu.edu.tw/api/galleryList/%d/' % (number,)


def getarturl(str):
    return 'http://hall.lib.nctu.edu.tw/api/artData/%s/' % (str,)


if __name__ == '__main__':
    Gallery.objects.all().delete()
    for i in range(1, 100):
        print("page is %d" % i)
        data = requests.get(getgalleryurl(i))
        data = json.loads(data.content.decode('utf-8'))
        if int(data['status']) != 200:
            break
        list = data['data']
        for item in list:
            serial = item['serial']
            cover = item['cover']
            data2 = requests.get(getarturl(item['serial']))
            data2 = json.loads(data2.content.decode('utf-8'))
            data2 = data2['data']
            title = data2['title']
            begin = data2['begin']
            end = data2['end']
            people = data2['people']
            place = data2['place']
            description = data2['description']
            try:
                gallery = Gallery.objects.create(serial=serial, title=title, begin=begin, end=end, people=people,
                                                 place=place, cover=cover,
                                                 description=description)
            except:
                continue

            items = data2['items']
            for It in items:
                Item.objects.create(serial=gallery, title=It['title'], imgPath=It['imgPath'])
