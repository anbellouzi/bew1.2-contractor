# Generated by Django 2.2.6 on 2019-12-04 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olive', '0014_auto_20191204_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_number',
            field=models.IntegerField(),
        ),
    ]
