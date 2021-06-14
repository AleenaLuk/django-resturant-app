from rest_framework import serializers

from .models import Resturant


class RestaurantSerializer(serializers.ModelSerializer):
     class Meta:
         model = Resturant

         fields = ('name', 'price', 'image')
