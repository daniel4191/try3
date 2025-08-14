from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("제목", max_length=50)
    name = models.CharField("작성자", max_length=50)
    content = models.TextField("내용")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)
    
    def __str__(self):
        return f"{self.id}번 작성 글: {self.title}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name="선택할 글", on_delete=models.CASCADE)
    comment = models.TextField("댓글내용")
    
    def __str__(self):
        return f"{self.id}번째 댓글 {self.post}에 관한 글"