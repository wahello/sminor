# Generated by Django 2.0.3 on 2018-06-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greinar', '0029_greinar_titletext'),
    ]

    operations = [
        migrations.AddField(
            model_name='greinar',
            name='image_size',
            field=models.CharField(choices=[('lítil', 'lítil'), ('stór', 'stór')], default=1, max_length=200),
        ),
    ]
