# Generated by Django 3.2.20 on 2023-07-23 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0007_alter_booked_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='treatment',
        ),
        migrations.DeleteModel(
            name='Treatment',
        ),
    ]