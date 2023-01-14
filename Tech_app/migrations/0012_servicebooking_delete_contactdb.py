# Generated by Django 4.1.4 on 2023-01-05 15:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0011_contactdb_booked_time_contactdb_slot_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aname', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('slot_status', models.CharField(default='Pending', max_length=200)),
                ('booked_time', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 5, 15, 29, 52, 521445))),
                ('date_for_service', models.DateField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tech_app.registerdb')),
            ],
        ),
        migrations.DeleteModel(
            name='Contactdb',
        ),
    ]
