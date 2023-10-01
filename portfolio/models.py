from django.db import models
from django.contrib.auth.models import User
from django.utils import  timezone
from PIL import Image
# Create your models here.
class Post(models.Model):
    img = models.ImageField(upload_to='post_picture')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    captions = models.TextField()
    time = models.DateTimeField(default=timezone.now())
    like = models.ManyToManyField(User, blank=True, related_name='like')

    def __str__(self):
        return f"{self.author.username}\'s Post - {self.title}"
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height>400 or img.width>400:
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    def Count_like(self):
        return self.like.count()
    def get_absolute_url(self):
        return reversed('post_detail',kwargs={'pk':self.pk})