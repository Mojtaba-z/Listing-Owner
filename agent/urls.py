from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('agent_listings', views.AgentListingsViewSet, basename='agent_listings')

urlpatterns = [
    path('', include(router.urls))
]