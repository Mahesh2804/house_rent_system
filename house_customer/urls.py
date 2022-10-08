from django.urls import path, include
from . import views

urlpatterns = [
    path('houses/houses_customerlogin/', views.houses_customerlogin, name='houses_customerlogin'),
    path('houses/houses_customerlogout/', views.houses_customerlogout, name='houses_customerlogout'),
    path('houses/houses_customerregister/', views.houses_customerregister, name='houses_customerregister'),
    path('houses/h_customer_home/', views.h_customer_home, name="h_customer_home"),
    path('houses/h_customer_profile/', views.h_customer_profile, name='h_customer_profile'),
    path('houses/h_customer_search/', views.h_customer_search, name='h_customer_search'),
    path('houses/h_customer_searchresults/', views.h_customer_searchresults, name='h_customer_searchresults'),
    path('houses/h_customer_renthouse/', views.h_customer_renthouse, name = 'h_customer_renthouse'),
    path('houses/h_customer_request/', views.h_customer_request, name = 'h_customer_request'),
    path('houses/h_confirm/', views.h_confirm, name = 'h_confirm'),
    path('houses/houses_customerbookings/', views.houses_customerbookings, name = 'houses_customerbookings'),
    
]