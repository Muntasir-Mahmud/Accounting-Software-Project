from django.forms import ModelForm
from . models import Order, Supplier_slip


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)
        self.fields['customer'].empty_label = "-- select --"
        self.fields['product'].empty_label = "-- select --"


class Supplier_slipForm(ModelForm):
    class Meta:
        model = Supplier_slip
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Supplier_slipForm,self).__init__(*args, **kwargs)
        self.fields['supplier'].empty_label = "-- select --"
        self.fields['product'].empty_label = "-- select --"

