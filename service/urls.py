from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.cars, name="cars"),
    path("cars/<int:pk>", views.car, name="car_details"),
    path("services/", views.ServiceListView.as_view(), name="services"),
    path("create_service/", views.create_service, name="create_service"),
    path("create_car_model/", views.create_car_model, name="create_car_model"),
    path("create_car/", views.create_car, name="create_car"),
    path("create_order/", views.create_order, name="create_order"),
    path("create_order_line/", views.create_order_line, name="create_order_line"),
]
