# Generated by Django 4.0.5 on 2022-07-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
