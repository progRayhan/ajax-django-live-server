# Generated by Django 4.1 on 2022-08-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('message', models.CharField(max_length=200, verbose_name='Message')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
            ],
        ),
    ]
