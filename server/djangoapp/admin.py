from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]
    
class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make', 'name', 'type', 'year', 'color']
    fields_filter = ['car_make']
    fields_search = ['car_make', 'name', 'type']

# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline


# Register models here

admin.site.register(CarMake)
admin.site.register(CarModel)
