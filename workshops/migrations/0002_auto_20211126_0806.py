# Generated by Django 3.2.6 on 2021-11-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='address_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='location',
        ),
        migrations.AddField(
            model_name='workshop',
            name='location',
            field=models.ManyToManyField(blank=True, related_name='workshops', to='workshops.Location'),
        ),
    ]
