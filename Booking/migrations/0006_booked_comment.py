# Generated by Django 3.2.20 on 2023-07-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0005_rename_free_slot_reserved'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked',
            name='comment',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
