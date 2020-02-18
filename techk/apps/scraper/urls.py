from django.urls import path, include, re_path
from . import views
from rest_framework import routers

# Default router w
router = routers.DefaultRouter()
# Register the category url 
router.register('categories',views.CategoryView, basename='Category')
# Register the books category
router.register('books',views.BookView, basename='Book')


urlpatterns = [
    path('',include(router.urls)),
    # Case for the books from categories
    # e.g /categories/3/books
    re_path(r'^categories/(?P<pk>[0-9]+)/books/$',  
            views.CategoryBooksView.as_view()),]