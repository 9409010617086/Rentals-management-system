# Generated by Django 4.0.2 on 2022-03-11 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_property', '0009_remove_maintanancenotice_unit'),
        ('work_order', '0006_workorder_work_order_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workorder',
            name='unit',
        ),
        migrations.AddField(
            model_name='workorder',
            name='building',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rental_property.building'),
            preserve_default=False,
        ),
    ]