# Generated by Django 3.0 on 2020-10-26 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_product_stock_previous_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_dena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier_pawna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(null=True)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Supplier')),
            ],
        ),
        migrations.RemoveField(
            model_name='supplier_credit',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='Customer_debit',
        ),
        migrations.DeleteModel(
            name='Supplier_credit',
        ),
    ]
