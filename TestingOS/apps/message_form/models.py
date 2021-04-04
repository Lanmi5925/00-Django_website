from django.db import models
from datetime import datetime
# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    email = models.EmailField(verbose_name="邮箱")
    message = models.TextField(verbose_name="留言信息")
    # m_date = models.DateField(verbose_name="留言时间", default=datetime.now)
    m_time = models.DateTimeField(verbose_name="留言时间", default=datetime.now)

    class Meta:
        verbose_name = "留言信息"
        verbose_name_plural = verbose_name
        db_table = "message"
