from .models import passengers,User
from .serializers import PassengersSerializer ,UserSerializer
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from .permission import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class passengershighlight(generics.GenericAPIView):
    queryset = passengers.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        passenger = self.get_object()
        return Response(passenger.highlighted)

@api_view(['GET','POST'])
def api_root(request, format=None):
    return Response({ 'login': reverse('crudapp:userLogin',request=request,format=format)
    ,'register': reverse('crudapp:register',request=request,format=format)
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class passengers_urd(generics.RetrieveUpdateDestroyAPIView):
    queryset = passengers.objects.all()
    serializer_class = PassengersSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
                
def responsedata(stat, message, data=None):
    if stat:
        return {
            "status":stat,
            "message":message,
            "data": data
        }
    else:
        return {
            "status":stat,
            "message":message,
        }

class UserLogin(TokenObtainPairView):
    token_obtain_pair = TokenObtainPairView.as_view()
    def post(self,request, *args,**kwargs):
        try:
            info = list(User.objects.filter(email=request.data.get("email")).values('_id','email', 'username', 'contact'))
            info = info[0]
        except:
            return Response({ 
  'register': reverse('crudapp:register',request=request,format=format)
    })
        if not request.data.get('email'):
            return Response(responsedata(False, "Email Id is required"), status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if not request.data.get("password"):
            return Response(responsedata(False, "Password is required"), status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if not User.objects.filter(email=request.data.get("email")).exists():
            return Response(responsedata(False, "No user found with this Email Id"), status=status.HTTP_404_NOT_FOUND)
        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
                data = serializer.validate(request.data)
                data.update({"Access-Control-Expose-Headers": "access"})
                data.update(info)

                if serializer.user.is_active:
                    return Response(responsedata(True, "Login Successfull", data), status=200)
                else:
                    return Response(responsedata(False, "Please Validate Your Email Id"), status=400)

class RegisterUser(TokenObtainPairView):
    token_obtain_pair = TokenObtainPairView.as_view()
    def post(self,request,*args,**kwargs):
        if request.data:
            request.POST._mutable = True
            data = request.data
            data['Pass'] = data.get('password')
            if User.objects.filter(email=data.get('email')).values().exists():
                response(responsedata(False,"User already present"),status= status.HTTP_409_CONFLICT)
            data['is_active'] = True
            serializer = UserSerializer(data=data)
            if serializer.is_valid(raise_exception=True):


                serializer.save()
                tokenserializer = TokenObtainPairSerializer(data={"email": request.data.get("email"), "password": request.data.get("password")})
                if tokenserializer.is_valid(raise_exception=True):
                    data = tokenserializer.validate({"email": request.data.get("email"), "password": request.data.get("password")})
                tempid = serializer.data.get("_id")
            else:
                return Response(responsedata(False, "Can't insert data"), status=400)
            respdata = {
                '_id':tempid,
                'data':data,
                'username':serializer.data['username'],
                'email':serializer.data['email'],
            }
            return Response(responsedata(True, "Data Inserted", respdata), status=200)
        else:
            return Response(responsedata(False, "No data provided"), status=412)

