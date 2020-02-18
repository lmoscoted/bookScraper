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

    def get_queryset(self):
        # Get the primary from the url
        # And get all the books for 
        # that category
        cat_id = self.kwargs.get('pk', None)
        if cat_id is not None:
            books_category =  Book.objects.filter(category_id=cat_id)
            return books_category
        else: # If not pk is provided, return []
            return Book.objects.none()