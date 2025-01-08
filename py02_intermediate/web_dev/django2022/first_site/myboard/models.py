from django.db import models

# Create your models here.
class Post(models.Model):    # 게시글 
    title = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 내용
    writer = models.CharField(max_length=20)  # 작성자
    date = models.DateTimeField()  # 작성일

    def __str__(self):
        return self.title


class Answer(models.Model):  # 답글 
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 게시글과 연결되는 외래키
    content = models.TextField() # 내용
    writer = models.CharField(max_length=20) # 작성자
    date = models.DateTimeField() # 작성일

    def __str__(self):
        return self.title