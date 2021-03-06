# Generated by Django 3.1.1 on 2021-03-25 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotexam', '0012_auto_20210325_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multisel',
            name='QuestionImage',
            field=models.ImageField(default='static/images/blank.jpg', upload_to='static/question_images/%Y/%m', verbose_name='题目图片'),
        ),
        migrations.AlterField(
            model_name='rightorwrong',
            name='QuestionImage',
            field=models.ImageField(default='static/images/blank.jpg', upload_to='static/question_images/%Y/%m', verbose_name='题目图片'),
        ),
        migrations.AlterField(
            model_name='singlesel',
            name='QuestionImage',
            field=models.ImageField(default='static/images/blank.jpg', upload_to='static/question_images/%Y/%m', verbose_name='题目图片'),
        ),
    ]
