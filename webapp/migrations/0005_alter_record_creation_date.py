# Generated by Django 5.0.3 on 2024-03-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_record_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
