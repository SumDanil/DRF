from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        lst1 = Women.objects.all().values()
        lst = Women.objects.all()
        for i in lst:
            print(f"{i.return_that_what_i_want()}")
        return Response({'posts': list(lst1)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': model_to_dict(post_new)})

    # {
    #     "title": "title_test",
    #     "content": "content_test",
    #     "cat_id": 2
    # }

# class WomenAPIView(generics.ListAPIView):
#     # queryset = Women.objects.all()
#     queryset = [i.return_that_what_i_want() for i in Women.objects.all()]
#     # print(f"{queryset_gen=}")
#     serializer_class = WomenSerializer
