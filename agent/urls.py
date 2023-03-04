from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('agent_listings', views.AgentListingsViewSet, basename='agent_listings')
router.register('manage_properties', views.ManageProperties, basename='manage_properties')

urlpatterns = [
    path('', include(router.urls))
]