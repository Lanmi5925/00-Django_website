from datetime import datetime

from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('male', '男'),
    ('female', '女')
)

class QuestionPaper(models.Model):
    PaperSerial = models.IntegerField(verbose_name="试卷中题目编号", default=0)
    QuestionID = models.IntegerField(verbose_name="试题原编号")
    QuestionType = models.CharField(verbose_name="试题类型", choices=(("single", "单选题"), ("multiple", "多选题"), ("rorw", "判断题")), max_length=20)
    UserAnswer = models.CharField(verbose_name="学生答案", max_length=5, null=True)
    Score = models.IntegerField(verbose_name="题目分值", default=4)
    Commence = models.IntegerField(verbose_name="系统评分")

    class Meta:
        db_table = 'questionpaper'
        verbose_name = "试卷信息"
        verbose_name_plural = verbose_name


class RightOrWrong(models.Model):
    QuestionDate = models.IntegerField(verbose_name="试题日期", default=20210316)
    QuestionID = models.IntegerField(verbose_name="题目编号", null=True)
    Question = models.TextField(verbose_name="题目内容", null=True)
    QuestionImage = models.ImageField(verbose_name="题目图片", upload_to="static/question_images/%Y/%m", blank=True, null=True)
    Answer = models.CharField(verbose_name="参考答案", max_length=5, null=True)
    Score = models.IntegerField(verbose_name="题目分值", default=2)

    class Meta:
        db_table = 'row'
        verbose_name = "判断题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.QuestionDate) + str(self.QuestionID)


class SingleSel(models.Model):
    QuestionDate = models.IntegerField(verbose_name="试题日期", default=20210316)
    QuestionID = models.IntegerField(verbose_name="题目编号", null=True)
    QuestionImage = models.ImageField(verbose_name="题目图片", upload_to="static/question_images/%Y/%m", blank=True, null=True)
    Question = models.TextField(verbose_name="题目内容", null=True)
    ChoiceA = models.TextField(verbose_name="选项A", null=True)
    ChoiceB = models.TextField(verbose_name="选项B", null=True)
    ChoiceC = models.TextField(verbose_name="选项C", null=True)
    ChoiceD = models.TextField(verbose_name="选项D", null=True)
    Answer = models.CharField(verbose_name="参考答案", max_length=5, null=True)
    Score = models.IntegerField(verbose_name="题目分值", default=2)

    class Meta:
        db_table = 'singlesel'
        verbose_name = "选择题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.QuestionDate) + str(self.QuestionID)


class MultiSel(models.Model):
    QuestionDate = models.IntegerField(verbose_name="试题日期", default=20210316)
    QuestionID = models.IntegerField(verbose_name="题目编号", null=True)
    Question = models.TextField(verbose_name="题目内容", null=True)
    QuestionImage = models.ImageField(verbose_name="题目图片", upload_to="static/question_images/%Y/%m", blank=True, null=True)
    ChoiceA = models.TextField(verbose_name="选项A", null=True)
    ChoiceB = models.TextField(verbose_name="选项B", null=True)
    ChoiceC = models.TextField(verbose_name="选项C", null=True)
    ChoiceD = models.TextField(verbose_name="选项D", null=True)
    Answer = models.CharField(verbose_name="参考答案", max_length=5, null=True)
    Score = models.IntegerField(verbose_name="题目分值", default=2)

    class Meta:
        db_table = 'multisel'
        verbose_name = "多选题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.QuestionDate) + str(self.QuestionID)


class Teacher(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    sex = models.CharField(verbose_name='性别', max_length=8, choices=GENDER_CHOICES, default='男')
    password = models.CharField(verbose_name='密码', max_length=20, default='111111')
    email = models.EmailField(verbose_name='邮箱', default=None)
    birthday = models.DateField(verbose_name='出生日期')

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    sex = models.CharField(verbose_name='性别', max_length=8, choices=GENDER_CHOICES, default='男')
    password = models.CharField(verbose_name='密码', max_length=20, default='12345678')
    birthday = models.DateField(verbose_name='出生日期')
    email = models.EmailField(verbose_name='邮箱', default=None)

    class Meta:
        db_table = 'student'
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Grade(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE, default='')
    GradeDate = models.DateField(verbose_name='成绩', default=datetime.now)
    grade = models.IntegerField(verbose_name='成绩')

    class Meta:
        db_table = 'grade'
        verbose_name = '成绩'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' %(self.sid, self.grade)


class Answer(models.Model):
    answer = models.CharField(verbose_name='学生答案', max_length=5)
