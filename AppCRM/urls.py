from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("clients/",views.client_list,name="Clients"),
    path("<int:client>/",views.client_info,name="Info"),
    path("<int:clientid>/updateclientinfo/", views.update_client_info,name="UpdateInfo"),

]

