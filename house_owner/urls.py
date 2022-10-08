from django.urls import path, include
from . import views

urlpatterns = [
    path('houses/houses_ownerlogin/', views.houses_ownerlogin, name='houses_ownerlogin'),
    path('houses/houses_ownerregister/', views.houses_ownerregister, name='houses_ownerregister'),
    path('houses/h_owner_home/', views.h_owner_home, name="h_owner_home"),
    path('houses/houses_ownerlogout/', views.houses_ownerlogout, name='houses_ownerlogout'),
    path('houses/h_owner_profile/', views.h_owner_profile, name='h_owner_profile'),
    path('houses/h_owner_requests/', views.h_owner_requests, name='h_owner_requests'),
    path('houses/h_owner_add/', views.h_owner_add, name='h_owner_add'),
    path('houses/h_owner_manage/', views.h_owner_manage, name='h_owner_manage'),
    path('houses/destroy/', views.destroy, name='destroy'),
    path('houses/update/', views.update, name='update'),    
]
