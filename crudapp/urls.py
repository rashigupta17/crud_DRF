from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
app_name = "crudapp"
urlpatterns = [
    path('', views.api_root),
    path('passenger/<int:pk>/highlight/', views.passengershighlight.as_view()),
    path('passenger/', views.passengers_list.as_view(),name= 'passenger_list'),
    path('passenger/<int:pk>/',views.passengers_urd.as_view()),
    path('boardingpass/', views.boarding_pass_list.as_view()),
    path('boardingpass/<int:pk>/',views.boarding_pass_urd.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
]
urlpatterns= format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]