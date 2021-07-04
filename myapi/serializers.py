from rest_framework import serializers

from .models import Hospital

class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'Hospital', 'County','City')