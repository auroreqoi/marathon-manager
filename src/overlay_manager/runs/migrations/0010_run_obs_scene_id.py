# Generated by Django 5.0.6 on 2024-05-23 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("runs", "0009_remove_eventdata_event_end_on_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="run",
            name="obs_scene_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
