# Generated by Django 5.0.3 on 2024-04-14 12:56

import building_app.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_app', '0001_initial'),
        ('handler_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('zipCode', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoardroomBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardroom_booking_id', models.CharField(blank=True, default=building_app.models.default_function, editable=False, max_length=14)),
                ('description', models.TextField()),
                ('startDate', models.CharField(max_length=200, null=True)),
                ('endDate', models.CharField(max_length=200, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_app.employee')),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building_app.building')),
            ],
        ),
        migrations.CreateModel(
            name='Boardroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardroom_id', models.CharField(blank=True, default=building_app.models.default_function, editable=False, max_length=14)),
                ('capacity', models.IntegerField()),
                ('address', models.CharField(max_length=200, null=True)),
                ('zipCode', models.CharField(max_length=200, null=True)),
                ('province', models.CharField(max_length=200, null=True)),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building_app.building')),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_id', models.CharField(blank=True, default=building_app.models.default_function, editable=False, max_length=14)),
                ('address', models.CharField(max_length=200, null=True)),
                ('zipCode', models.CharField(max_length=200, null=True)),
                ('province', models.CharField(max_length=200, null=True)),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building_app.building')),
            ],
        ),
        migrations.CreateModel(
            name='BoardroomBookingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building_app.boardroombooking')),
                ('boadroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building_app.parking')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(blank=True, default=building_app.models.default_function, editable=False, max_length=14)),
                ('description', models.TextField()),
                ('startDate', models.DateTimeField(max_length=200, null=True)),
                ('endDate', models.DateTimeField(max_length=200, null=True)),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building_app.building')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingBookingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building_app.parkingbooking')),
                ('parking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building_app.parking')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.CharField(blank=True, default=building_app.models.default_function, editable=False, max_length=14)),
                ('description', models.TextField()),
                ('reportedDate', models.CharField(max_length=200, null=True)),
                ('handledDate', models.CharField(max_length=200, null=True)),
                ('handlerSolution', models.TextField()),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building_app.building')),
                ('handler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='handler_app.handler')),
                ('reporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_app.employee')),
            ],
        ),
    ]
