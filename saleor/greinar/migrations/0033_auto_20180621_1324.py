# Generated by Django 2.0.3 on 2018-06-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greinar', '0032_auto_20180621_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greinar',
            name='image_size',
            field=models.CharField(choices=[('lítil', 'Lítil'), ('stór', 'Stór')], default='lítil', max_length=20),
        ),
    ]
