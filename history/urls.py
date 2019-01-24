from django.urls import path
from . import views

app_name = 'history'
urlpatterns = [
    # ex: /artists/
    path('', views.index, name='index'),   
    path('<int:artistid_id>/', views.detail, name='detail'),
    path('addNewArtist/', views.newArtist, name='addArtist'),
]