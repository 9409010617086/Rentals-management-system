# Generated by Django 4.0.2 on 2022-03-12 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_tenants_rented_unit'),
        ('core', '0027_managertenantcommunication_send_to_all_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managertenantcommunication',
            name='sent_to',
        ),
        migrations.AddField(
            model_name='managertenantcommunication',
            name='sent_to',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.tenants'),
            preserve_default=False,
        ),
    ]
