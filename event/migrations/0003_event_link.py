# Generated by Django 5.1.2 on 2024-11-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
