# Generated by Django 2.0.3 on 2018-06-19 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greinar', '0003_auto_20180619_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='greinar',
            name='Greinar_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
