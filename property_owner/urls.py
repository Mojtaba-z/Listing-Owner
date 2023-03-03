from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('property', views.PropertyViewSet, basename='property')
router.register('property_type', views.PropertyTypeViewSet, basename='property_type')
router.register('room', views.RoomViewSet, basename='room')
router.register('room_options', views.RoomOptionsViewSet, basename='room_options')
router.register('amenities', views.AmenitiesViewSet, basename='amenities')

urlpatterns = [
    path('', include(router.urls))
]