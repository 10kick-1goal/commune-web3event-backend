# Generated by Django 5.0.3 on 2024-04-07 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventurl',
            name='type',
        ),
        migrations.AddField(
            model_name='eventurl',
            name='site_type',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='eventurl',
            name='source_url',
            field=models.CharField(max_length=200),
        ),
    ]
