from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CarForm, CarModelForm, OrderForm, OrderLineForm, ServiceForm
from .models import Car, Order, Service


def index(request):
    num_cars = Car.objects.all().count()
    num_services = Service.objects.all().count()
    # TODO filter only completed orders
    num_orders = Order.objects.all().count()

    context = {
        "num_cars": num_cars,
        "num_services": num_services,
        "num_orders": num_orders,
    }
    return render(request, "service/index.html", context)


def create_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("create_service"))
    else:
        form = ServiceForm()
    context = {"form": form, "action_url": reverse("create_service")}
    return render(request, "service/generic_form.html", context)


def create_car_model(request):
    if request.method == "POST":
        form = CarModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("create_car_model"))
    else:
        form = CarModelForm()
    context = {"form": form, "action_url": reverse("create_car_model")}
    return render(request, "service/generic_form.html", context)


def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("create_car"))
    else:
        form = CarForm()
    context = {"form": form, "action_url": reverse("create_car")}
    return render(request, "service/generic_form.html", context)


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("create_order"))
    else:
        form = OrderForm()
    context = {"form": form, "action_url": reverse("create_order")}
    return render(request, "service/generic_form.html", context)


def create_order_line(request):
    if request.method == "POST":
        service = Service.objects.get(pk=int(request.POST["service"]))
        request_data = {
            "order": request.POST["order"],
            "service": request.POST["service"],
            "price": str(service.price),
            "quantity": request.POST["quantity"],
        }
        form = OrderLineForm(request_data)
        if form.is_valid():
            form.save()
            order = Order.objects.get(pk=form.cleaned_data["order"].id)
            order.total_price = (
                F("total_price")
                + form.cleaned_data["price"] * form.cleaned_data["quantity"]
            )
            order.save()
            return HttpResponseRedirect(reverse("create_order_line"))
    else:
        form = OrderLineForm()
    context = {"form": form, "action_url": reverse("create_order_line")}
    return render(request, "service/order_line_form.html", context)
