from django.contrib import admin
from .models import Product, Order, Cart, Wishlist, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'total_price', 'payment_method', 'ordered_at')
    list_filter = ('payment_method', 'ordered_at')
    search_fields = ('user__username', 'full_name', 'email')
    inlines = [OrderItemInline]


admin.site.register(Product)
#admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(OrderItem)
