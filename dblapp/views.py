from rest_framework import viewsets, permissions
from dblapp.models import ItemRecord, OrgRecord, FactoryRecord
from dblapp.serializers import (
    ItemRecordSerializer,
    OrgRecordSerializer,
    FactoryRecordSerializer,
)


class FactoryRecordViewSet(viewsets.ModelViewSet):
    queryset = FactoryRecord.objects.all()
    serializer_class = FactoryRecordSerializer
    permission_classes = [permissions.AllowAny]


class OrgRecordViewSet(viewsets.ModelViewSet):
    queryset = OrgRecord.objects.all()
    serializer_class = OrgRecordSerializer
    permission_classes = [permissions.AllowAny]


class ItemRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ItemRecord.objects.all()
    serializer_class = ItemRecordSerializer
