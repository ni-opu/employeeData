# Generated by Django 4.0.4 on 2022-04-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
                ('employee_id', models.CharField(max_length=50)),
                ('shift', models.CharField(choices=[('General', 'General'), ('Night', 'Night'), ('Morning', 'Morning'), ('Evening', 'Evening')], max_length=50)),
                ('arrival', models.CharField(choices=[('Late', 'Late'), ('On time', 'On time')], max_length=70)),
                ('remark', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
