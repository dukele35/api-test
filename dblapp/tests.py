from django.test import TestCase
from model_bakery import baker
from dblapp.models import FactoryRecord, OrgRecord
from pprint import pprint


class FactoryRecordTestCase(TestCase):
    def setUp(self):
        self.factory = baker.make("FactoryRecord")
        pprint(self.factory.__dict__)

    def test_model_str(self):
        factory = FactoryRecord.objects.create(factory_name="Fac1")
        self.assertIs(type(str(factory)), str)


class OrgRecordTestCase(TestCase):
    def setUp(self):
        self.org = baker.make("OrgRecord")
        pprint(self.org.__dict__)

    def test_model_str(self):
        org = OrgRecord.objects.create(org_name="Org1")
        self.assertIs(type(str(org)), str)
