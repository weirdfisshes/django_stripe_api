from django.contrib import admin

from .models import Item, Order

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price') 
    search_fields = ('name',) 
    list_filter = ('price',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'amount') 
    search_fields = ('item',) 
    list_filter = ('amount',)

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)