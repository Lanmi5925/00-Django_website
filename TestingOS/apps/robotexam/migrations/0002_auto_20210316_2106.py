# Generated by Django 3.1.1 on 2021-03-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotexam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multisel',
            name='QuestionImage',
            field=models.ImageField(null=True, upload_to='question_images/%Y/%m', verbose_name='题目图片'),
        ),
        migrations.AddField(
            model_name='rightorwrong',
            name='QuestionImage',
            field=models.ImageField(null=True, upload_to='question_images/%Y/%m', verbose_name='题目图片'),
        ),
        migrations.AddField(
            model_name='singlesel',
            name='QuestionImage',
            field=models.ImageField(null=True, upload_to='question_images/%Y/%m', verbose_name='题目图片'),
        ),
    ]
