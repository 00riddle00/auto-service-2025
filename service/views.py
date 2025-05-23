import pandas as pd
import plotly.express as px
import plotly.offline as po
from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .forms import CarForm, CarModelForm, OrderForm, OrderLineForm, ServiceForm
from .models import Car, Order, Service


def index(request):
    num_cars = Car.objects.all().count()
    num_services = Service.objects.all().count()
    num_orders = Order.objects.filter(status__exact="C").count()

    df = pd.DataFrame(
        {
            "items": ["Cars", "Services", "Orders"],
            "count": [num_cars, num_services, num_orders],
        }
    )
    fig = px.bar(
        df,
        x="items",
        y="count",
        color_discrete_sequence=["#386b58"],
        title="Overview:",
    )
    fig.update_layout(xaxis_title=None, yaxis_title=None)
    fig.update_yaxes(dtick=1, ticks="outside", tickwidth=2, tickformat=",d")
    bar_chart = po.plot(fig, output_type="div")

    context = {
        "num_cars": num_cars,
        "num_services": num_services,
        "num_orders": num_orders,
        "bar_chart": bar_chart,
    }
    return render(request, "service/index.html", context)


def cars(request):
    paginator = Paginator(Car.objects.all().order_by("id"), per_page=4)
    page_number = request.GET.get("page")
    paged_cars = paginator.get_page(page_number)
    return render(request, "service/cars.html", context={"cars": paged_cars})


def car(request, pk):
    car_ = get_object_or_404(Car, pk=pk)
    return render(request, "service/car_details.html", context={"car": car_})


class ServiceListView(generic.ListView):
    model = Service
    paginate_by = 4
    context_object_name = "services"
    template_name = "service/services.html"
    ordering = ["id"]


class ServiceDetailView(generic.DetailView):
    model = Service
    context_object_name = "service"
    template_name = "service/service_details.html"


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 4
    context_object_name = "orders"
    template_name = "service/orders.html"
    ordering = ["id"]


class OrderDetailView(generic.DetailView):
    model = Order
    context_object_name = "order"
    template_name = "service/order_details.html"


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
