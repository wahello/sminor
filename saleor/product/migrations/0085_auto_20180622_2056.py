# Generated by Django 2.0.3 on 2018-06-22 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0084_auto_20180622_2054'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]