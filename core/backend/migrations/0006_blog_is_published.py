# Generated by Django 4.0.5 on 2022-07-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_subscriber_alter_contact_contact_alter_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
