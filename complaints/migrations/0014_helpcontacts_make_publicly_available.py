# Generated by Django 4.0.2 on 2022-03-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0013_helpcontacts_associated_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpcontacts',
            name='make_publicly_available',
            field=models.BooleanField(default=False),
        ),
    ]
