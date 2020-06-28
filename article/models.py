from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArticlePost(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    body = models.TextField(verbose_name='正文')
    created = models.DateTimeField(default=timezone.now, verbose_name='发表时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        ordering = ('-created',)
        verbose_name = '文章'

    def __str__(self):
        return self.title

