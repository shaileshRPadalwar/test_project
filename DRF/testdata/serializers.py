from rest_framework import serializers

from .models import MakeAppointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeAppointment
        fields = '__all__'