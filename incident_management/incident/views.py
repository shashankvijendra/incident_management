from django.shortcuts import render
from rest_framework.views import APIView
from .models import Incidents, Handlers
from .serializer import IncidentSerializer
from rest_framework.response import Response
from rest_framework import status
from .common import WorkStatus

# Create your views here.


class IncidentAPIView(APIView):
    
    def get(self,request):
        incident=Incidents.objects.all()
        serialize=IncidentSerializer(incident,many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def post(self,request,pk):
        if available_handler := Handlers.objects.filter(assignment_count=0
                        ).order_by('-modified_on'):
                request.data['status'] = WorkStatus.WORKING
                request.data['assigned_to'] = available_handler[0].name
        serialize=IncidentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request, pk):
        data=request.data
        serialize = IncidentSerializer(data=data)
        if serialize.is_valid():
            
            incident=Incidents.objects.filter(incident_id=pk).first()
            if not incident:
                return Response(serialize.data,status=status.HTTP_404_NOT_FOUND)
            serialize.update(incident, data)
            return Response(serialize.data,status=status.HTTP_200_OK)  
        
    
