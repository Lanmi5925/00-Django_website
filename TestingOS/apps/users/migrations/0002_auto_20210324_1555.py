# Generated by Django 3.1.1 on 2021-03-24 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '超级用户', 'verbose_name_plural': '超级用户'},
        ),
    ]
