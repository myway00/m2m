from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default = timezone.now)
    body = models.TextField(default='')
class Comment(models.Model):
    objects=models.Manager()
    #참조할 것은 콘텐트(외래키로 알려주기), on delete는 삭제를 할 시에 그것과 연달아서 삭제가 될 것
    #댓글 삭제시 연동이 되어야 하니깐 cascade 를 사용해주는 것
    post=models.ForeignKey('Content', on_delete=models.CASCADE)
    text=models.TextField(default='')
    created_date=models.DateTimeField(default=timezone.now)
