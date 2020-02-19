# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, generics, mixins

from .models import Category, Book
from .serializer import CategorySerializer, BookSerializer
from .scraping import get_data_scrapper


def startScraper(request):
    ''''
    First, delete all registers in both
    categories and book table, then start 
    the sraper and finally, store the data
    into the DB.
    '''
    #Delete all records in the category table 
    # (truncate)
    Category.objects.all().delete()
    # Delete all records in the book table 
    # (truncate)
    Book.objects.all().delete()

    # Data from the scrapper (books and categories)
    scraper_data = get_data_scrapper()
    categories = scraper_data['categories']
    books = scraper_data['books']

    

    # Save categories into DB 
    for category in categories:
        category_db = Category(**category)
        category_db = category_db.save()
    # Save books into DB    
    for book in books:
        book_db = Book(**book)
        book_db = book_db.save()

    return HttpResponse('Scraping done!')



#---------------API----------------------------
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