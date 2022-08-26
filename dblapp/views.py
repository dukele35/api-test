from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from dblapp.serializers import UserSerializer
from dblapp.models import FactoryRecord
from dblapp.serializers import FactoryRecordSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class FactoryRecordList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = FactoryRecord.objects.all()
    serializer_class = FactoryRecordSerializer

class FactoryRecordDetail(generics.RetrieveAPIView, generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = FactoryRecord.objects.all()
    serializer_class = FactoryRecordSerializer
