from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    # ModelViewSet - fot work with model. This class give functionals for GET, POST, PUT, RETRIVE, DELETE
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # get_queryset - use fore custom  return value in get query
    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            list = Women.objects.filter(cat__name='Певицы')
            print(f"{list=}")
            return list

        return Women.objects.filter(pk=pk)

    # this add one more rout in this class http://127.0.0.1:8000/api/v1/women/category/
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
#     if you want return list in response you must rewrite code on code below
#     @action(methods=['get'], detail=False)
#     def category(self, request, pk=None):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})


# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
