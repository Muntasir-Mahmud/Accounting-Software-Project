from django.contrib import admin

from . models import Customer, Order, Product, Product_stock, Customer_dena, Supplier, Supplier_slip, Supplier_pawna

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Product_stock)
admin.site.register(Customer_dena)
admin.site.register(Supplier)
admin.site.register(Supplier_slip)
admin.site.register(Supplier_pawna)