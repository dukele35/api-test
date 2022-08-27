import random
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

def random_string_1():
    return str(random.randint(10000, 99999))

def random_string_2():
    return str(random.randint(1000, 9999))

class FactoryRecord(models.Model):
    factory_id = models.CharField(max_length=5,primary_key = True, unique=True, default = random_string_1, editable = False)
    factory_name = models.CharField(max_length=20)

    def __str__(self):
        return self.factory_id

class OrgRecord(models.Model):
    org_id = models.CharField(max_length=4,primary_key = True, unique=True, default = random_string_2, editable = False)
    org_name = models.CharField(max_length=20)

    def __str__(self):
        return self.org_id

class ItemRecord(models.Model):
    COUNTRY_CHOICES = [
        ("VN", "Vietnam"),
        ("MY", "Malaysia"),
        ("PH", "Philippines"),
        ("SG", "Singapore"),
        ("TH", "Thailand"),
    ]
    # factory_id = models.CharField(max_length=5,primary_key = True, unique=True, default = random_string_1, editable = False)
    factory_id = models.ForeignKey(FactoryRecord,on_delete=models.CASCADE)
    org_id = models.ForeignKey(OrgRecord,on_delete=models.CASCADE)
    country = models.CharField(max_length=10,choices=COUNTRY_CHOICES,default="VN", blank=True)
    execution_date = models.DateField(null=True, blank=True)
    fail_rate = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    defect_rate = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    # def __str__(self):
    #     return self.factory_id

    # class Meta:
    #     ordering = ['factory_id']
