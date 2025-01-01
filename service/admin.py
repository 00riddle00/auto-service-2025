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
    list_editable = ["observations"]
    list_filter = ["client_name", "car_model__make", "car_model__model"]
    search_fields = ["license_plate_number", "vin_code"]


class CarModelAdmin(admin.ModelAdmin):
    list_display = ["make", "model", "year", "engine_type", "fuel_type", "description"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "description"]
    list_editable = ["description"]


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]
    inlines = [OrderLineInline]
    list_display = ["car", "date", "total_price", "status"]
    list_editable = ["status"]


admin.site.register(Car, CarAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
