# Generated by Django 3.1.7 on 2021-10-03 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_sender_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('msg_sender_email', models.EmailField(blank=True, default='', max_length=70, null=True)),
                ('msg_content', models.TextField(blank=True, default='', null=True)),
                ('msg_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Date')),
            ],
        ),
    ]
