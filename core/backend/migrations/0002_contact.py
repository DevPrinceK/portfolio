# Generated by Django 4.0.5 on 2022-07-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(max_length=200)),
                ('contact', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
