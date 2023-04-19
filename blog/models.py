from django.db import models
from authentication_app.models import AuthUser
from django.contrib.auth import get_user_model
from django.utils import timezone


class Post(models.Model):
    
    def post_directory_path(instance, filename):    
        return 'blog/media/{0}/{1}/{2}'.format(instance.post_author.username,instance.title,filename)
    
    title = models.CharField(max_length=250,)
    # -------------------------------------------
    post_slug  = models.SlugField(max_length=250,)
    # -------------------------------------------
    post_author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    # -------------------------------------------
    post_header_image = models.ImageField(upload_to=post_directory_path,null=True,blank=True)
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
    
    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['title','post_author'], name='unique_title_and_author')
    ]
        
    # -------------------------------------------       
    
    def __str__(self):
        return self.title
    
    # ------------------------------------------- 
    

# ============================================================
# ============================================================


class PostImage(models.Model):
    def post_image_directory_path(instance, filename):    
        return '{0}/{1}/{2}'.format(instance.post.post_author.username,instance.post.title,filename)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # -------------------------------------------
    image = models.FileField(upload_to=post_image_directory_path)
    # -------------------------------------------
    
    def __str__(self):
        return 'image_{}-for post "{}"'.format(self.id,self.post)


# ============================================================
# ============================================================


class PostComment(models.Model):
    post         = models.ForeignKey(Post,on_delete=models.CASCADE)
    # -------------------------------------------
    user         = models.ForeignKey(get_user_model(),on_delete=models.PROTECT)
    # -------------------------------------------
    comment      = models.CharField(max_length=500)
    # -------------------------------------------
    active       = models.BooleanField(default=False)
    # -------------------------------------------
    created_date = models.DateTimeField(auto_now_add=True)
    # -------------------------------------------

    def __str__(self) :
        return "{} - {} by {} ".format(self.pk,self.comment,self.user)
