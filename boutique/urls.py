from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('produit/<slug:slug>/', views.produit_detail, name='produit_detail'),
    path('contact/', views.contact, name='contact'),
]
