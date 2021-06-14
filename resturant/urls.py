from django.urls import path

from .views import ResturantListAPIView

urlpatterns = [
    path('', ResturantListAPIView.as_view(), name="resturant_list")
]
