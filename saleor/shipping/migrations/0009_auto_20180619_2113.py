# Generated by Django 2.0.3 on 2018-06-19 21:13

from django.db import migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0008_auto_20180108_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='price',
            field=django_prices.models.MoneyField(currency='ISK', decimal_places=0, max_digits=12),
        ),
    ]
