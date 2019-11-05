# Generated by Django 2.2.6 on 2019-11-04 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maths', models.IntegerField()),
                ('science', models.IntegerField()),
                ('english', models.IntegerField()),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Student')),
            ],
        ),
    ]
