from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from api.models import *
from api.serializers import *
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', ])
def gallerylist(request, page=None, year=None):
    if page is None:
        page = 1
    query_set = None
    if year:
        query_set = Gallery.objects.filter(begin__year=year)
    else:
        query_set = Gallery.objects.all()
    paginator = Paginator(query_set, 20)
    if paginator.num_pages < int(page):
        data = dict()
        data['status'] = '404'
        data['error'] = 'no this page'
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        result = paginator.page(page)
        serializer = GalleyGetSerializer(result, many=True)
        data = dict()
        data['data'] = serializer.data
        data['status'] = '200'
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def artdata(request, serial):
    try:
        gallery = Gallery.objects.get(serial=serial)
    except:
        data = dict()
        data['status'] = '404'
        data['error'] = 'not found'
        return Response(data=data, status=status.HTTP_200_OK)
    galleryserializer = GalleyDataSerializer(gallery)
    itemserializer = ItemSerializer(gallery.items, many=True)
    data = dict()
    data['data'] = galleryserializer.data
    data['data']['items'] = itemserializer.data
    return Response(data=data, status=status.HTTP_200_OK)
