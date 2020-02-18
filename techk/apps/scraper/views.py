# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, generics, mixins

from .models import Category, Book
from .serializer import CategorySerializer, BookSerializer
