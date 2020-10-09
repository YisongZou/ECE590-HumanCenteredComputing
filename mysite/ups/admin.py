from django.contrib import admin

# Register your models here.

from .models import Package
from .models import Product
from .models import Truck

admin.site.register(Package)
admin.site.register(Product)
admin.site.register(Truck)
