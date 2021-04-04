# Generated by Django 3.1.1 on 2021-03-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotexam', '0004_auto_20210316_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multisel',
            name='Answer',
            field=models.CharField(max_length=5, null=True, verbose_name='参考答案'),
        ),
        migrations.AlterField(
            model_name='multisel',
            name='ChoiceA',
            field=models.TextField(null=True, verbose_name='选项A'),
        ),
        migrations.AlterField(
            model_name='multisel',
            name='ChoiceB',
            field=models.TextField(null=True, verbose_name='选项B'),
        ),
        migrations.AlterField(
            model_name='multisel',
            name='ChoiceC',
            field=models.TextField(null=True, verbose_name='选项C'),
        ),
        migrations.AlterField(
            model_name='multisel',
            name='ChoiceD',
            field=models.TextField(null=True, verbose_name='选项D'),
        ),
        migrations.AlterField(
            model_name='multisel',
            name='Question',
            field=models.TextField(null=True, verbose_name='题目内容'),
        ),
        migrations.AlterField(
            model_name='multisel',
            name='QuestionID',
            field=models.IntegerField(max_length=10, null=True, verbose_name='题目编号'),
        ),
        migrations.AlterField(
            model_name='multisel',
            name='Score',
            field=models.IntegerField(default=2, null=True, verbose_name='题目分值'),
        ),
        migrations.AlterField(
            model_name='rightorwrong',
            name='Answer',
            field=models.CharField(max_length=5, null=True, verbose_name='参考答案'),
        ),
        migrations.AlterField(
            model_name='rightorwrong',
            name='Question',
            field=models.TextField(null=True, verbose_name='题目内容'),
        ),
        migrations.AlterField(
            model_name='rightorwrong',
            name='QuestionID',
            field=models.IntegerField(max_length=10, null=True, verbose_name='题目编号'),
        ),
        migrations.AlterField(
            model_name='rightorwrong',
            name='Score',
            field=models.IntegerField(default=2, null=True, verbose_name='题目分值'),
        ),
        migrations.AlterField(
            model_name='singlesel',
            name='Answer',
            field=models.CharField(max_length=5, null=True, verbose_name='参考答案'),
        ),
        migrations.AlterField(
            model_name='singlesel',
            name='ChoiceA',
            field=models.TextField(null=True, verbose_name='选项A'),
        ),
        migrations.AlterField(
            model_name='singlesel',
            name='ChoiceB',
            field=models.TextField(null=True, verbose_name='选项B'),
        ),
        migrations.AlterField(
            model_name='singlesel',
            name='ChoiceC',
            field=models.TextField(null=True, verbose_name='选项C'),
        ),
        migrations.AlterField(
            model_name='singlesel',
            name='ChoiceD',
            field=models.TextField(null=True, verbose_name='选项D'),
        ),
        migrations.AlterField(
            model_name='singlesel',
            name='Question',
            field=models.TextField(null=True, verbose_name='题目内容'),
        ),
        migrations.AlterField(
            model_name='singlesel',
            name='QuestionID',
            field=models.IntegerField(max_length=10, null=True, verbose_name='题目编号'),
        ),
        migrations.AlterField(
            model_name='singlesel',
            name='Score',
            field=models.IntegerField(default=2, null=True, verbose_name='题目分值'),
        ),
    ]
