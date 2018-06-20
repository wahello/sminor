# Generated by Django 2.0.3 on 2018-06-19 21:13

from django.db import migrations, models
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0047_order_line_name_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount_amount',
            field=django_prices.models.MoneyField(currency='ISK', decimal_places=0, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='language_code',
            field=models.CharField(default='is', max_length=35),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_price_gross',
            field=django_prices.models.MoneyField(currency='ISK', decimal_places=0, default=0, editable=False, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_price_net',
            field=django_prices.models.MoneyField(currency='ISK', decimal_places=0, default=0, editable=False, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_gross',
            field=django_prices.models.MoneyField(currency='ISK', decimal_places=0, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_net',
            field=django_prices.models.MoneyField(currency='ISK', decimal_places=0, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='unit_price_gross',
            field=django_prices.models.MoneyField(currency='ISK', decimal_places=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='unit_price_net',
            field=django_prices.models.MoneyField(currency='ISK', decimal_places=0, max_digits=12),
        ),
    ]
