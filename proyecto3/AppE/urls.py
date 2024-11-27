from django.urls import path
from AppE import views

urlpatterns = [
    path('inicio/', views.inicio, name= 'inicio' ),
    path('guitarras/', views.guitarras, name= 'guitarras'),
    path('provedor/', views.provedor, name= 'provedor'),
    path('vendedor/', views.vendedor, name= 'vendedor'),
    path('guitarra-form/', views.guitarra_form , name='GuitarrasForm'),
    path('busquedaModelo/', views.busquedaModelo, name='BusquedaModelo'),
    path('vendedor-form',views.vendedor_form, name= 'VendedorForm'),
    path('provedor-form',views.provedor_form, name= 'ProvedorForm'),
    path('buscar/', views.buscar, )
    
    ]