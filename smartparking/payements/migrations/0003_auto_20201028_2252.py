# Generated by Django 3.1.2 on 2020-10-28 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payements', '0002_auto_20201028_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
