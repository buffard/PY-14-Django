from django.urls import path
from . import views

urlpatterns = [
    # ex: /artists/
    path('', views.index, name='index'),   
    path('<int:artistid_id>/', views.detail, name='detail'),
]