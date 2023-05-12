from django.db import models
import uuid

class Client(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    Surname = models.CharField(max_length=20, blank=False,default='')
    Name = models.CharField(max_length=20, blank=False,default='')
    Patronic = models.CharField(max_length=20, blank=False,default='', null=True)

class SpecialistAdress(models.Model):
    City = models.CharField(max_length=20, blank=False,default='')
    Street = models.CharField(max_length=20, blank=False,default='')
    House = models.CharField(max_length=10, blank=False,default='')
    ID_specialist = models.CharField(max_length=40, blank=False,default='')
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)

class ClientContactDetails(models.Model):
    ID_contact_categories = models.CharField(max_length=40, blank=False,default='')
    Contact = models.CharField(max_length=40, blank=False,default='')
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)

class Specialist(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    Surname = models.CharField(max_length=20, blank=False, default='')
    Name = models.CharField(max_length=20, blank=False, default='')
    Patronic = models.CharField(max_length=20, blank=False, default='', null=True)

class SpecialistContactDetails(models.Model):
    ID_contact_categories = models.CharField(max_length=40, blank=False, default='')
    Contact = models.CharField(max_length=40, blank=False, default='')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Recording_window(models.Model):
    Start_time = models.TimeField(blank=True, null=True)
    End_time = models.TimeField(blank=True, null=True)
    Date = models.TimeField(blank=True, null=True)
    ID_specialist = models.CharField(max_length=40, blank=False,default='')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ID_client = models.CharField(max_length=40, blank=False, default='')

class procedure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_procedure = models.CharField(max_length=40, blank=False, default='')
    description = models.CharField(max_length=300, blank=False, default='')

class specialist_procedure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ID_specialist = models.CharField(max_length=40, blank=False, default='')
    ID_procedure = models.CharField(max_length=40, blank=False, default='')

class contact_categories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_category = models.CharField(max_length=40, blank=False, default='')

# Create your models here.
