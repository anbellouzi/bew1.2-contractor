# Generated by Django 2.2.6 on 2019-12-03 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olive', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Date order was made', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='Date when order updated', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.CharField(help_text='Your email', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(help_text='John Doe', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_number',
            field=models.IntegerField(help_text='###-###-####', unique=True),
        ),
    ]