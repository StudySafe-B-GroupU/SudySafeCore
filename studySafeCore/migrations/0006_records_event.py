# Generated by Django 4.0.4 on 2022-05-02 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studySafeCore', '0005_alter_records_hku_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='event',
            field=models.CharField(default='Entry', max_length=5),
        ),
    ]
