# Generated by Django 2.2.6 on 2019-10-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('roll_no', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
    ]
