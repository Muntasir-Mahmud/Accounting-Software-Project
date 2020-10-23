from django.shortcuts import render, redirect
from . models import  Customer, Order, Product, Product_stock, Customer_debit, Supplier, Supplier_slip, Supplier_credit
from . forms  import OrderForm, Supplier_slipForm
from . filters import OrderFilter, CustomerFilter

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    context = {'orders': orders, 'customers': customers}

    return render(request, 'crm/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request, 'crm/products.html',{'products' : products})

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customers.html',{'customers' : customers})


def customer_detail(request,pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = CustomerFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders':orders,'order_count':order_count, 'myFilter': myFilter}
    return render(request, 'crm/customer_detail.html', context) 


def orders(request):
    orders = Order.objects.all()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'orders' : orders, 'myFilter': myFilter}

    return render(request, 'crm/orders.html', context)


def createOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            product = form.cleaned_data['product']
            product_stock = Product_stock.objects.get(product=product)
            product_stock.quantity -= form.cleaned_data['total_ream']
            print(product_stock.quantity)
            product_stock.save()
            return redirect('/orders/')

    context = {'form': form}
    return render(request,'crm/order_form.html', context)


def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/orders/')


    context = {'form': form}
    return render(request,'crm/order_form.html', context)


def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/orders/')

    context = {'item': order}
    return render(request,'crm/delete.html',context)


def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'crm/suppliers.html',{'suppliers' : suppliers})


def supplier_slip_list(request):
    supplier_slip_list = Supplier_slip.objects.all()

    # myFilter = OrderFilter(request.GET, queryset=orders)
    # orders = myFilter.qs

    context = {'supplier_slip_list' : supplier_slip_list}

    return render(request, 'crm/supplier_slip_list.html', context)


def createSupplier_slip(request):

    form = Supplier_slipForm()
    if request.method == 'POST':
        form = Supplier_slipForm(request.POST)
        if form.is_valid():
            form.save()
            product = form.cleaned_data['product']
            product_stock = Product_stock.objects.get(product=product)
            product_stock.quantity += form.cleaned_data['total_ream']
            print(product_stock.quantity)
            product_stock.save()
            return redirect('/supplier_slip_list/')

    context = {'form': form}
    return render(request,'crm/supplier_slip_form.html', context)




def updateSupplier_slip(request, pk):

    supplier_slip = Supplier_slip.objects.get(id=pk)
    form = Supplier_slipForm(instance=supplier_slip)

    if request.method == 'POST':
        form = Supplier_slipForm(request.POST, instance=supplier_slip)
        if form.is_valid():
            form.save()
            return redirect('/supplier_slip_list/')

    context = {'form': form}
    return render(request,'crm/supplier_slip_form.html', context)


def deleteSupplier_slip(request, pk):

    supplier_slip = Supplier_slip.objects.get(id=pk)
    if request.method == 'POST':
        supplier_slip.delete()
        return redirect('/supplier_slip_list/')

    context = {'item': supplier_slip}
    return render(request,'crm/delete_supplier_slip.html',context)


def stocks(request):

    stock = Product_stock.objects.all()

    return render(request, 'crm/stock.html', {'stock' : stock})


def stock_detail(request):
    orders = Order.objects.all()
    supplier_slip_list = Supplier_slip.objects.all()

    context = {'orders': orders, 'supplier_slip_list': supplier_slip_list}

    return render(request, 'crm/stock_detail.html', context)









