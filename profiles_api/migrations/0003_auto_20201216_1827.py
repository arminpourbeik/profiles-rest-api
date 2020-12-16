# Generated by Django 3.1.4 on 2020-12-16 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilefeeditem',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
