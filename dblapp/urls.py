from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'item', views.ItemRecordViewSet)
router.register(r'org', views.OrgRecordViewSet)


urlpatterns = [
    path('', include(router.urls))
]
