# Generated by Django 4.2.6 on 2023-10-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_successful_execution_time', models.DateTimeField()),
            ],
        ),
    ]