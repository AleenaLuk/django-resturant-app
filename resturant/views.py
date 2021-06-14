from rest_framework import generics
# Create your views here.
from .models import Resturant
from .serializers import RestaurantSerializer
# Create your views here.

class ResturantListAPIView(generics.ListAPIView):
    queryset = Resturant.objects.all()
    serializer_class = RestaurantSerializer
# class ResturantList(generics.List):
