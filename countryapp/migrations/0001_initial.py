# Generated by Django 5.0 on 2024-06-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('country_code', models.CharField(max_length=30)),
                ('iso_codes', models.CharField(max_length=30)),
                ('population', models.CharField(max_length=50)),
                ('area_km2', models.CharField(max_length=50)),
                ('gdp_usd', models.CharField(max_length=30)),
                ('capital', models.CharField(max_length=50)),
            ],
        ),
    ]