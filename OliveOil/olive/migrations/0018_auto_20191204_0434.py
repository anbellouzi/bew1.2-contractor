# Generated by Django 2.2.6 on 2019-12-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olive', '0017_auto_20191204_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
