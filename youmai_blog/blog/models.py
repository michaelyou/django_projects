#encoding=UTF-8
from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:         #Meta是一个内部类
        ordering = ['timestamp',]    #用元组或数组都可以
    
    
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'timestamp')
    
    

    
    
admin.site.register(BlogPost, BlogPostAdmin)