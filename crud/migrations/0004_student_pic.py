# Generated by Django 2.2.6 on 2019-11-14 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20191105_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pic',
            field=models.ImageField(default='images/blank.png', upload_to='images/'),
        ),
    ]