# Generated by Django 4.2 on 2023-07-03 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lyra', '0006_rename_simulationrun_run_actions_run_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actions',
            new_name='Action',
        ),
    ]