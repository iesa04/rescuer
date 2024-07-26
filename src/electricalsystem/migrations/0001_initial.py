# Generated by Django 4.2.7 on 2023-11-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricalSystem',
            fields=[
                ('electrical_id', models.IntegerField(primary_key=True, serialize=False)),
                ('electrical_name', models.CharField(max_length=30, unique=True)),
                ('electrical_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]