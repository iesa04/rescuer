# Generated by Django 4.2.7 on 2023-11-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chassis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('chassis_name', models.CharField(max_length=20)),
                ('frontal_airbags', models.CharField(max_length=20)),
                ('seating_capacity', models.IntegerField()),
                ('side_roll_protection', models.CharField(max_length=15)),
                ('front_gawr', models.IntegerField()),
                ('rear_gawr', models.IntegerField()),
                ('chassis_cost', models.IntegerField()),
            ],
        ),
    ]
