from operator import mod
from django.db import models
import random
import uuid

# def random_string():
#     return str(random.randint(10000, 99999))

class FactoryRecord(models.Model):
    factory_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    country = models.CharField(max_length=5,blank=True)

    # def __str__(self):
    #     return self.factory_id

    # class Meta:
    #     ordering = ['factory_id']