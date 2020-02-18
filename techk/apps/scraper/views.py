# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, generics, mixins

from .models import Category, Book
from .serializer import CategorySerializer, BookSerializer


# Class view for only list, delete categories
class CategoryView(mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = CategorySerializer 
    queryset = Category.objects.all()                


# Class view for only delete books
class BookView(mixins.DestroyModelMixin,
                viewsets.GenericViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()


# Class view for only list the books from
# a specific category
class CategoryBooksView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()