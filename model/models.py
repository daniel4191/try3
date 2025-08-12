from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("제목", max_length=50)
    name = models.CharField("작성자", max_length=50)
    content = models.TextField("내용")
    
    def __str__(self):
        return f"{self.id}번 작성 글: {self.title}"