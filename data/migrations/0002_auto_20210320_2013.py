# Generated by Django 2.2 on 2021-03-20 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='csvdata',
            options={'ordering': ['country']},
        ),
    ]