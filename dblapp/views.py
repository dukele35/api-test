from rest_framework import viewsets, permissions
from dblapp.models import FactoryRecord, OrgRecord
from dblapp.serializers import FactoryRecordSerializer, OrgRecordSerializer

class OrgRecordViewSet(viewsets.ModelViewSet):
    queryset = OrgRecord.objects.all()
    serializer_class = OrgRecordSerializer
    permission_classes = [permissions.AllowAny]

class FactoryRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = FactoryRecord.objects.all()
    serializer_class = FactoryRecordSerializer
