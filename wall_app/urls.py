from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('message/delete', views.delete_message),
    path('message/create', views.create_message),
    path('comment/delete', views.delete_comment),
    path('comment/create', views.create_comment), 
]