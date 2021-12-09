from django.urls import path

from . import views

urlpatterns = [
    path('api/listas/<int:lista_id>/', views.api_lista),
    path('api/listas/', views.api_all),
]