import random
import string
from django.db import models
from authentication_app.models import AuthUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from autoslug import AutoSlugField


ID_SIZE = 8

def id_generator(size=ID_SIZE, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Post(models.Model):
    
    def post_directory_path(instance, filename):    
        return 'blog/media/{0}/{1}/{2}'.format(instance.post_author.username,instance.title,filename)
    
    id = models.CharField(max_length=ID_SIZE, primary_key=True, default=id_generator, editable=False)
    # -------------------------------------------
    title = models.CharField(max_length=45,)
    # -------------------------------------------
    post_slug = AutoSlugField(
        populate_from=lambda instance: f'{instance.id}-{instance.title}',
        max_length=100, 
        unique=True)
    # -------------------------------------------
    post_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # -------------------------------------------
    post_header_image = models.ImageField(upload_to=post_directory_path, null=True, blank=True)
    # -------------------------------------------
    create_date = models.DateTimeField(auto_now_add=True)
    # -------------------------------------------
    publish_date = models.DateTimeField(default=timezone.now)
    # -------------------------------------------
    update_date  = models.DateTimeField(auto_now=True)
    # -------------------------------------------
    POST_STATUSES = (
        ('published','PUBLISHED'),
        ('draft','DRAFT'),
    )
    post_status = models.CharField(max_length=10, choices=POST_STATUSES, default='draft')
    # -------------------------------------------
    
    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['title','post_author'], name='unique_title_and_author')
    ]
        
    # -------------------------------------------       
    
    def __str__(self):
        return self.title
    
    # ------------------------------------------- 
    

# ============================================================


class PostParagraph(models.Model):
    def post_image_directory_path(instance, filename):    
        return 'blog/media/{0}/{1}/P_{2}/{3}'.format(instance.post.post_author.username,instance.post.title,instance.topic,filename)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='paragraphs')
    # -------------------------------------------
    topic = models.CharField(max_length=100)
    # -------------------------------------------
    content = models.TextField(max_length=2000, null=True, blank=True)
    # -------------------------------------------
    order = models.PositiveSmallIntegerField()
    # -------------------------------------------
    header_image = models.ImageField(upload_to=post_image_directory_path,null=True,blank=True)
    # -------------------------------------------
    
    class Meta:
        ordering = ['order']


# ============================================================


class PostComment(models.Model):
    post         = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # -------------------------------------------
    user         = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    # -------------------------------------------
    comment      = models.TextField(max_length=300)
    # -------------------------------------------
    active       = models.BooleanField(default=False)
    # -------------------------------------------
    created_date = models.DateTimeField(auto_now_add=True)
    # -------------------------------------------

    def __str__(self) :
        return "{} - {} by {} ".format(self.pk,self.comment,self.user)
