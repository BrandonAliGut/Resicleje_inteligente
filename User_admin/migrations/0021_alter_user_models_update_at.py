# Generated by Django 4.2.4 on 2023-10-04 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_admin', '0020_alter_user_models_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_models',
            name='update_at',
            field=models.DateField(default=datetime.datetime(2023, 10, 3, 22, 16, 53, 752251)),
        ),
    ]
