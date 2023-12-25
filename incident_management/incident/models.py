from django.db import models
import uuid

# Create your models here.


class Handlers(models.Model):
    
    name = models.CharField(max_length=200)
    modified_on = models.DateTimeField(auto_created=True,auto_now=True)
    assignment_count = models.IntegerField(default=0)

class Incidents(models.Model):
    
    incident_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(max_length=200)
    severity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=50, default='Pending')
    assigned_to = models.CharField(max_length=200,blank=True)
