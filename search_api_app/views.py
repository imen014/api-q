from django.shortcuts import render
from search_api_app.serializers import DataSerializer
from search_api_app.models import Data
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size =1000

class DataView(ModelViewSet):
    pagination_class = Paginator
    serializer_class=DataSerializer

    def get_queryset(self,*args,**kwargs):
        queryset = Data.objects.all()
        title = self.request.GET.get('title')
        dispo = self.request.GET.get('dispo')
        if title:
            queryset=queryset.filter(title=title)
        elif dispo:
            dispo.lower()
            if dispo=="true":
                queryset=queryset.filter(dispo=True)
            if dispo=="false":
                queryset=queryset.filter(dispo=False)
        return queryset