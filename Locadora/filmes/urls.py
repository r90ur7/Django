from django.urls import path
from filmes import views
app_name = "filmes"
urlpatterns=[
    path('filme/',views.list_filmes, name ='list_filmes'),
    path('New/',views.New_filmes, name ='New_filmes'),
    path('Delete/<int:pk>/',views.Del_filmes, name ='Del_filmes'),
    path('Edit/<int:pk>/',views.Edit_filmes, name ='Edit_filmes'),
    path('', views.index, name='index'),
]


