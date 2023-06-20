# Generated by Django 4.2 on 2023-06-14 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Interval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_intervall', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin_no', models.CharField(max_length=100)),
                ('engine_no', models.CharField(max_length=100)),
                ('last_service', models.IntegerField()),
                ('current_milage', models.IntegerField()),
                ('service_intervall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service_interval')),
                ('v_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.v_model')),
                ('vehicle_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.make')),
            ],
        ),
    ]
