# Generated by Django 2.2.6 on 2019-12-04 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olive', '0016_auto_20191204_0407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='number',
            new_name='phone_number',
        ),
    ]