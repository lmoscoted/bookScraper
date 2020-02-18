from rest_framework import serializers
from .models import Category, Book


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:       
        model = Category
        fields = ('id','name')


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:     
        model = Book
        fields = ('id','title','product_description','price',
                    'category_id','upc','stock','thumbnail')