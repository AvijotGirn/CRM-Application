from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("customers/",views.cust_list,name="Customers"),
    path("custinfo/",views.cust_notes,name="Info"),

]

