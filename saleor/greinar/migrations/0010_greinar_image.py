# Generated by Django 2.0.3 on 2018-06-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greinar', '0009_auto_20180620_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='greinar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='greinar_myndir/'),
        ),
    ]
