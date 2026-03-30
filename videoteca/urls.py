from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('giochi/', views.lista_giochi, name='lista'),
    path('giochi/<int:id>/', views.dettaglio_gioco, name='dettaglio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('aggiungi/', views.aggiungigioco, name='aggiungi'),
    path('modifica/<int:id>/', views.modificagioco, name='modifica'),
    path('elimina/<int:id>/', views.eliminagioco, name='elimina'),
]