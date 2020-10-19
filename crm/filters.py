import django_filters
from django_filters import DateFilter, CharFilter


from . models import *

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'debit_amount', 'total_ream', 'total_money','date_created']

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['debit_amount', 'total_ream', 'total_money','date_created']