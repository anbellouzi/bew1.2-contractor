# Generated by Django 2.2.6 on 2019-12-04 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('olive', '0011_auto_20191204_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
