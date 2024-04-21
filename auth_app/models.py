from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
class Post(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
  
    def __str__(self):
        return self.title
    
    def shorten(self):
        return self.title[:30] + '...'
    
    def get_absolute_url(self):
        return reverse('prop_detail', args=[str(self.id)])
    
class Otzivlar(models.Model):

    img = models.ImageField()
       
    def get_absolute_url(self):
        return reverse('otziv_detail', args=[str(self.id)])



class Natijalar(models.Model):

    img = models.ImageField()
       
    def get_absolute_url(self):
        return reverse('natija_detail', args=[str(self.id)])


 
class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE  
    ) 
    def str(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('pages.urls')

class Statistika(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length = 120)
    description = models.TextField()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('statistika', args=[str(self.id)])

class Tarif(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length = 120)
    description = models.TextField()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tarif', args=[str(self.id)])