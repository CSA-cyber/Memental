# Generated by Django 3.2 on 2021-04-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0006_auto_20210421_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='edutation',
            field=models.TextField(blank=True, null=True),
        ),
    ]