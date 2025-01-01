from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    price = models.FloatField(blank=False, null=False)
    description = models.TextField(max_length=4096, default="")

    def __str__(self):
        return f"{self.name} ({self.price})"


class CarModel(models.Model):
    make = models.CharField(max_length=30, blank=False, null=False)
    model = models.CharField(max_length=50, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    engine_type = models.CharField(max_length=40, blank=False, null=False)
    fuel_type = models.CharField(max_length=64)
    description = models.TextField(max_length=4096, default="")

    def __str__(self):
        return f"{self.make} ({self.model} {self.year})"


class Car(models.Model):
    car_model = models.ForeignKey(
        CarModel, on_delete=models.RESTRICT, blank=False, null=False
    )
    license_plate_number = models.CharField(max_length=15, blank=False, null=False)
    vin_code = models.CharField(max_length=17, blank=False, null=False, unique=True)
    client_name = models.CharField(max_length=70, blank=False, null=False)
    observations = models.TextField(max_length=2048, default="")

    def __str__(self):
        return f"{self.client_name} ({self.license_plate_number} {self.car_model.make})"


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.RESTRICT, blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    NEW = "N"
    DECLINED = "D"
    ACCEPTED = "A"
    IN_PROGRESS = "P"
    COMPLETED = "C"
    ORDER_STATUSES = {
        NEW: "New",
        DECLINED: "Declined",
        ACCEPTED: "Accepted",
        IN_PROGRESS: "In Progress",
        COMPLETED: "Completed",
    }
    status = models.CharField(
        max_length=1, choices=ORDER_STATUSES, default=NEW, blank=True
    )

    def __str__(self):
        return f"{self.car.license_plate_number} ({self.date} {self.total_price})"

    @property
    def total_price(self):
        total_price = 0
        for line in self.lines.all():
            total_price += line.price
        return total_price


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.RESTRICT, blank=False, null=False, related_name="lines"
    )
    service = models.ForeignKey(
        Service, on_delete=models.RESTRICT, blank=False, null=False
    )
    quantity = models.IntegerField(default=1, blank=False, null=False)

    def __str__(self):
        return f"{self.service.name} ({self.quantity})"

    @property
    def price(self):
        return self.service.price * self.quantity
