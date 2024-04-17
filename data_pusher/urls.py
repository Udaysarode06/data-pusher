# urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('accounts', views.AccountViewSet)
router.register('destinations', views.DestinationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('server/incoming_data/', views.incoming_data, name='incoming_data'),
]