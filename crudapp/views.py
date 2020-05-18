from .models import passengers
from .serializers import PassengersSerializer ,UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import permissions
from .permission import IsOwnerOrReadOnly
from rest_framework import renderers

class passengershighlight(generics.GenericAPIView):
    queryset = passengers.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        passenger = self.get_object()
        return Response(passenger.highlighted)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('crudapp:user-list', request=request, format=format),
        'passenger': reverse('crudapp:passenger-list', request=request, format=format),
        'pass': reverse('crudapp:pass-list', request=request, format=format)
    })
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class passengers_list(generics.ListCreateAPIView):
    queryset = passengers.objects.all()
    serializer_class = PassengersSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        

    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class passengers_urd(generics.RetrieveUpdateDestroyAPIView):
    queryset = passengers.objects.all()
    serializer_class = PassengersSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]