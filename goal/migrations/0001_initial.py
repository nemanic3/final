# Generated by Django 5.1.5 on 2025-02-05 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('goal_type', models.CharField(choices=[('annual', '연간 목표'), ('monthly', '월간 목표')], default='annual', max_length=10)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'goal',
            },
        ),
    ]
