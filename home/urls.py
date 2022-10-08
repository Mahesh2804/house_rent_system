from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexpage, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),    
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallerypage2/', views.gallerypage2, name='gallerypage2'),
    
    path('gallerypage3/', views.gallerypage3, name='gallerypage3'),
    
    path('houses/', views.houses_home, name='houses_home'),
    path('vehicles/', views.vehicles_home, name='vehicles_home'),
]
