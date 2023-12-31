# Generated by Django 4.0.3 on 2023-12-25 11:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handlers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_on', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Incidents',
            fields=[
                ('incident_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('severity', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('assigned_to', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
