# Generated by Django 2.0.3 on 2018-06-22 09:49

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0075_auto_20180622_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributechoicevalue',
            name='litur',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
    ]
