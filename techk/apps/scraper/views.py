# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets, generics, mixins

from .models import Category, Book
from .serializer import CategorySerializer, BookSerializer
from .scraping import get_data_scrapper


@transaction.atomic
def startScraper(request):
    ''''
    First, delete all registers in both
    categories and book table, then start 
    the sraper and finally, store the data
    into the DB.
    '''

    # Data from the scrapper (books and categories)
    scraper_data = get_data_scrapper()
    categories = scraper_data['categories']
    books = scraper_data['books']

    # Create categories and book instances lists from
    # the data gotten from the scraper
    category_instances = [Category(**category) 
                        for category in categories]
    book_instances = [Book(**book) for book in books]

    # Clean and insert the new records.
    cleanPopulateDB(book_instances,category_instances)

    return HttpResponse('Scraping done!')


def cleanPopulateDB(book_instances,category_instances):
    '''
    Clean the old records and insert the new records
    '''
    #Delete old records in the category and book
    #  table 
    # (truncate)
    Category.objects.all().delete()
    Book.objects.all().delete()

    # Bulk insert with the new data
    Category.objects.bulk_create(category_instances)
    Book.objects.bulk_create(book_instances)



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