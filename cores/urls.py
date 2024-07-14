from django.contrib import admin
from django.urls import path
from .views import OrderView
from . import views

urlpatterns = [
    path("api/orders/", OrderView.as_view(), name="api_orders"),
    path("", views.order_form, name="home"),
]
