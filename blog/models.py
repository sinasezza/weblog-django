import string
import random
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from authentication_app.models import AuthUser 

ID_SIZE = 8

def id_generator(size=ID_SIZE, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_post_slug(instance):
    return f'{instance.id}-{instance.title}'

def post_directory_path(instance, filename):    
    return f'blog/media/{instance.author.username}/{instance.title}/{filename}'
    

class Post(models.Model):
    id = models.CharField(max_length=ID_SIZE, primary_key=True, default=id_generator, editable=False)
    title = models.CharField(max_length=45)
    slug = AutoSlugField(populate_from=generate_post_slug, max_length=100, unique=True)
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='posts')
    header_image = models.ImageField(upload_to=post_directory_path, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    POST_STATUSES = (('published', 'PUBLISHED'), ('draft', 'DRAFT'))
    status = models.CharField(max_length=10, choices=POST_STATUSES, default='draft')


    def __str__(self):
        return self.title
    

class PostParagraph(models.Model):
    def post_image_directory_path(instance, filename):    
        return f'blog/media/{instance.post.author.username}/{instance.post.title}/P_{instance.topic}/{filename}'
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='paragraphs')
    topic = models.CharField(max_length=40)
    content = models.TextField(max_length=1000, null=True, blank=True)
    order = models.PositiveSmallIntegerField()
    header_image = models.ImageField(upload_to=post_image_directory_path, null=True, blank=True)

    class Meta:
        ordering = ['order']

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(AuthUser, on_delete=models.PROTECT)
    comment = models.TextField(max_length=300)
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.comment} by {self.user}"
