# Generated by Django 3.0.2 on 2020-04-07 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('location_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomesApp.Location')),
            ],
        ),
    ]
