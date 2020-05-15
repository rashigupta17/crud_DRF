from rest_framework import serializers
from .models import boardingpass,passengers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    passenger = serializers.PrimaryKeyRelatedField(many=True, queryset=passengers.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'passenger']


class PassengersSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = passengers
        fields = ["name","contact","boardingid", "owner"]


class BoardingPassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = boardingpass
        fields = ["flightdate","id","added_by"]



class PassengersSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = passengers
        fields = ["name","contact","boardingid", "owner"]

