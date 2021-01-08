from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self): #id 대신 subject 이름으로 출력
        return self.subject

    class Meta:
        verbose_name = '게시판'
        verbose_name_plural = '북마크 모음'
        ordering = ['create_date']
        db_table = 'board'

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    class Meta:
        verbose_name = '게시판 답글'
        verbose_name_plural = '북마크 모음'
        ordering = ['create_date']
        db_table = 'board answer'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '댓글'
        db_table = 'comment'