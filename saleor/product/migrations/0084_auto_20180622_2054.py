# Generated by Django 2.0.3 on 2018-06-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0083_attributechoicevalue_litur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Greinar',
            field=models.ManyToManyField(blank=True, null=True, related_name='greinar', to='greinar.greinar'),
        ),
    ]
