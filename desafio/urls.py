from django.urls import path
from .views import una_vista, un_template

urlpatterns = [
    path('', una_vista, name='index'),
    path('mi-template/', un_template, name='mi_template'),
]