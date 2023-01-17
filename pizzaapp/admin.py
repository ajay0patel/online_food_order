from django.contrib import admin
from .models import OrderModel,PizzaModel,CustomerModel
# Register your models here.
admin.site.register(OrderModel)
admin.site.register(PizzaModel)
admin.site.register(CustomerModel)