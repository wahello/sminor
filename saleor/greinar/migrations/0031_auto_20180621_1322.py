# Generated by Django 2.0.3 on 2018-06-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greinar', '0030_greinar_image_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greinar',
            name='image_size',
            field=models.CharField(choices=[('Lítil', 'lítil'), ('Stór', 'stór')], default=1, max_length=20),
        ),
    ]
