from rest_framework import serializers
from dblapp.models import FactoryRecord, OrgRecord


class OrgRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgRecord
        fields = "__all__"

class FactoryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryRecord
        fields = "__all__"
