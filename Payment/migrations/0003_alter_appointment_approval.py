# Generated by Django 3.2 on 2021-04-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_alter_appointment_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]
