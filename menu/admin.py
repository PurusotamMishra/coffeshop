from django.contrib import admin
from menu.models import CakeMenu, CoffeeMenu, TeaMenu


# Register your models here.


admin.site.register(CoffeeMenu)
admin.site.register(TeaMenu)
admin.site.register(CakeMenu)
