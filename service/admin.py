from django.contrib import admin

from .models import Car, CarModel, Order, OrderLine, Service


class CarAdmin(admin.ModelAdmin):
    list_display = [
        "car_model",
        "license_plate_number",
        "vin_code",
        "client_name",
        "observations",
    ]
    list_editable = ["client_name"]
    list_filter = ["client_name", "car_model__make", "car_model__model"]
    search_fields = ["license_plate_number", "vin_code"]


class CarModelAdmin(admin.ModelAdmin):
    list_display = ["make", "model", "year", "engine_type"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]
    inlines = [OrderLineInline]
    list_display = ["car", "date", "total_price", "status"]
    list_editable = ["total_price", "status"]


admin.site.register(Car, CarAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
