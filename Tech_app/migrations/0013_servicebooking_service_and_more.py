# Generated by Django 4.1.2 on 2023-01-08 15:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0012_servicebooking_delete_contactdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicebooking',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tech_app.service'),
        ),
        migrations.AlterField(
            model_name='servicebooking',
            name='booked_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 8, 15, 8, 46, 789551)),
        ),
        migrations.CreateModel(
            name='ServiceStatusDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_rendered', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.IntegerField()),
                ('images', models.ImageField(upload_to='images')),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tech_app.servicebooking')),
            ],
        ),
    ]
