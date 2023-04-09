from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250,)
    # -------------------------------------------
    post_slug  = models.SlugField(max_length=250,)
    # -------------------------------------------
    post_author = models.ForeignKey(User,on_delete=models.CASCADE)
    # -------------------------------------------
    header_image = models.ImageField(upload_to=f'{title}',null=True,blank=True)
    # -------------------------------------------
    body = models.TextField()
    # -------------------------------------------
    create_date = models.DateTimeField(auto_now_add=True)
    # -------------------------------------------
    publish_date = models.DateTimeField(default=timezone.now)
    # -------------------------------------------
    update_date  = models.DateTimeField(auto_now=True)
    # -------------------------------------------
    status_choices = (
        ('published','PUBLISHED'),
        ('draft','DRAFT'),
    )
    post_status = models.CharField(max_length=10,choices=status_choices,default='draft')
    # -------------------------------------------
    

# ============================================================
# ============================================================

