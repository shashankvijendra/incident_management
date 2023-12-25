from rest_framework import serializers
from .models import Incidents


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = ['type','severity',
                  'timestamp', 'description', 'status', 'assigned_to']
        
    
    def create(self, validated_data):
        return Incidents.objects.create(**validated_data)
    
class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = ['type','severity',
                  'timestamp', 'description', 'status', 'assigned_to']
        
    
    def create(self, validated_data):
        return Incidents.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        if validated_data.get('status'):
            instance.status = validated_data.get('status')
        if validated_data.get('assigned_to'):
            instance.assigned_to = validated_data.get('assigned_to')   
        instance.save()

