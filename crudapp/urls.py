from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
app_name = "crudapp"
urlpatterns= format_suffix_patterns([path('', views.api_root),
    #path('passenger/<int:pk>/highlight/', views.passengershighlight.as_view()),
    path('passenger/', views.passengers_list.as_view(),name= 'passenger-list'),
    path('passenger/<int:pk>/',views.passengers_urd.as_view(),name="passenger-detail"),
    path('passenger/<int:pk>/highlight/',views.passengershighlight.as_view(),name="passenger-highlight"),
    path('users/', views.UserList.as_view(),name= 'user-list' ),
    path('users/<int:pk>/', views.UserDetail.as_view(),name= 'user-detail'),
    #path('superadminlogin', views.SuperAdminLogin.as_view(), name='superadminlogin'),
    path('userlogin', views.UserLogin.as_view(), name='userlogin'),
    path('register', views.RegisterUser.as_view(), name='register'),
    

])
