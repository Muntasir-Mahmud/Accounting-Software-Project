# Generated by Django 3.0.8 on 2020-07-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20200708_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_stock',
            name='previous_quantity',
            field=models.IntegerField(null=True),
        ),
    ]
