from django.forms import ModelForm

from .models import Car, CarModel, Order, OrderLine, Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class CarModelForm(ModelForm):
    class Meta:
        model = CarModel
        fields = "__all__"


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["car"]


class OrderLineForm(ModelForm):
    class Meta:
        model = OrderLine
        fields = "__all__"
