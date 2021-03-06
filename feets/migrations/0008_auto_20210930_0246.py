# Generated by Django 3.2.6 on 2021-09-30 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feets', '0007_auto_20210930_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='feet',
            name='activity',
            field=models.ManyToManyField(related_name='feets', to='feets.Activity'),
        ),
    ]
