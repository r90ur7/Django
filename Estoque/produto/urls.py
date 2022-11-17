from django.urls import path
from produto import views
app_name = "Produtos"
urlpatterns = [
    path('listar/',views.listar,name='listar'),
    path('novo/',views.novo,name='novo'),
    path('alterar/<int:pk>',views.novo,name='novo'),
    path('deletar/<int:pk>',views.deletar,name='novo'),
    path('alterar/<int:pk>',views.deletar,name='novo'),
]