from rest_framework import serializers
from dblapp.models import ItemRecord, OrgRecord


class OrgRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgRecord
        fields = "__all__"

class ItemRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRecord
        fields = "__all__"
