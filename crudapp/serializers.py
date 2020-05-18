from rest_framework import serializers
from .models import passengers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='passenger-detail', read_only=True)

    class Meta:
        model = User
        fields = ["url",'id', 'username', 'passenger']


class PassengersSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='passenger-highlight', format='html')
    class Meta:
        model = passengers
        fields = ["url","id","name","contact","boardingid", "owner"]


