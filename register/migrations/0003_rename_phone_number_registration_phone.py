# Generated by Django 5.0.2 on 2024-03-01 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_registration_session'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='phone_number',
            new_name='phone',
        ),
    ]