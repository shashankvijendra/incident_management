# Generated by Django 4.0.3 on 2023-12-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0003_alter_incidents_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]