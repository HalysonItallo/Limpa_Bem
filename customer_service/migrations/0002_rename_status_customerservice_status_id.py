# Generated by Django 4.1.7 on 2023-02-14 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerservice',
            old_name='status',
            new_name='status_id',
        ),
    ]