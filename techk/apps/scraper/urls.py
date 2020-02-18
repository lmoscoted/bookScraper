from django.urls import path, include, re_path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('categories',views.CategoryView, basename='Category')
router.register('books',views.BookView, basename='Book')


urlpatterns = [
    path('',include(router.urls)),]