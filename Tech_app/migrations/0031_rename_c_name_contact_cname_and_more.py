# Generated by Django 4.1.2 on 2023-01-11 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0030_remove_servicestatusdetail_images_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='c_name',
            new_name='cname',
        ),
        migrations.AlterField(
            model_name='servicebooking',
            name='booked_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 8, 14, 10, 776069)),
        ),
    ]
