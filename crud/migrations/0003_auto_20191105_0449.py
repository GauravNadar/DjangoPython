# Generated by Django 2.2.6 on 2019-11-05 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_marks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks',
            old_name='roll_no',
            new_name='student',
        ),
    ]
