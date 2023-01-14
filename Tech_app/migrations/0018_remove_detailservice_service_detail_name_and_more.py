# Generated by Django 4.1.2 on 2023-01-08 15:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0017_alter_servicebooking_booked_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailservice',
            name='service_detail_name',
        ),
        migrations.RemoveField(
            model_name='detailservice',
            name='slot_status',
        ),
        migrations.RemoveField(
            model_name='detailservice',
            name='time_required',
        ),
        migrations.AddField(
            model_name='servicebooking',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tech_app.service'),
        ),
        migrations.AddField(
            model_name='servicebooking',
            name='service_detail_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='servicebooking',
            name='time_required',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='servicebooking',
            name='booked_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 8, 15, 38, 29, 102289)),
        ),
    ]
