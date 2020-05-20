from rest_framework import serializers
from .models import passengers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    is_following = serializers.SerializerMethodField()

    def get_is_following(self,obj):
        try:
            userdata    = self.context.get('userdata')
            user_id     = userdata['_id']
            following   = Follow.objects.filter(user_from=user_id, user_to=obj._id)
            if not following:
                return False
            else:
                return True
        except Exception as e:
            return None

class PassengersSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='passenger-highlight', format='html')
    class Meta:
        model = passengers
        fields = ["url","id","name","contact","boardingid"]


