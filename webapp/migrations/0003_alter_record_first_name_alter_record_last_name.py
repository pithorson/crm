# Generated by Django 5.0.3 on 2024-03-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_firt_name_record_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='record',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
