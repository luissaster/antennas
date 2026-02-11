from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_csv, name='upload_csv'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('map/', views.map_view, name='map_view'),
    path('api/antennas/', views.antenna_data, name='antenna_data'),
]
