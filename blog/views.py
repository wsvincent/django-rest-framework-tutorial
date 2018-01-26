from rest_framework import generics

from . import models
from . import serializers


class BlogList(generics.ListAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
