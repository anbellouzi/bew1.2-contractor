from django.urls import path

from . import views

app_name = 'olive'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:olive_id>/', views.detail, name='detail'),
]
