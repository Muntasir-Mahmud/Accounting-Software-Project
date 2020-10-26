from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    gms = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product_stock(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True)
    previous_quantity = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, null= True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null= True, on_delete= models.SET_NULL)
    delivery_place = models.CharField(max_length=200, null=True)
    total_ream = models.IntegerField(null=True)
    total_money = models.IntegerField(null=True)
    debit_amount = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Customer_dena(models.Model):
    customer = models.ForeignKey(Customer, null= True, on_delete= models.SET_NULL)
    amount = models.IntegerField(null=True)


class Supplier(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Supplier_slip(models.Model):
    supplier = models.ForeignKey(Supplier, null= True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null= True, on_delete= models.SET_NULL)
    delivery_place = models.CharField(max_length=200, null=True)
    total_ream = models.IntegerField(null=True)
    total_money = models.IntegerField(null=True)
    debit_amount = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Supplier_pawna(models.Model):
    supplier = models.ForeignKey(Supplier, null= True, on_delete= models.SET_NULL)
    Amount = models.IntegerField(null=True)
