from rest_framework import serializers
from .models import passengers,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PassengersSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='passenger-highlight', format='html')
    class Meta:
        model = passengers
        fields = ["url","id","name","contact","boardingid", "owner"]


