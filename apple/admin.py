from django.contrib import admin

from .models import bikes,branches,orders

admin.site.register(bikes)
admin.site.register(branches)
admin.site.register(orders)
