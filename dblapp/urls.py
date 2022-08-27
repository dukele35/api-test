from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'factory', views.FactoryRecordViewSet)
router.register(r'org', views.OrgRecordViewSet)


urlpatterns = [
    path('', include(router.urls))
]
