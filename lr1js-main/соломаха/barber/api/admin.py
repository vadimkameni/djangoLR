from django.contrib import admin
from .models import Services, Orders


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_order', 'services', 'nickname',
                    'age', 'description', 'owner')
    list_display_links = ('id', 'date_of_order', 'services', 'nickname',
                          'age', 'description', 'owner')




