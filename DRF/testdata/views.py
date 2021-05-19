from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MakeAppointment
from .serializers import AppointmentSerializer
 
@api_view(['GET', 'POST'])
class Task_list(request):
    if request.method == 'GET':
        contacts = MakeAppointment.objects.all()
        serializer = AppointmentSerializer(contacts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)