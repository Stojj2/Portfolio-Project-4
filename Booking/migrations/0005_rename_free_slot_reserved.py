# Generated by Django 3.2.20 on 2023-07-22 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0004_auto_20230722_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slot',
            old_name='free',
            new_name='reserved',
        ),
    ]