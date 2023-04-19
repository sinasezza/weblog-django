from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthUser(AbstractUser):
    
    def user_directory_path(instance, filename):    
        return 'authentication_app/media/{0}/Profile_image/{1}'.format(instance.username,filename)
    
    age          = models.PositiveSmallIntegerField(default=0 , null=True,blank=True)
    # ------------------------------------------
    bio          = models.TextField(max_length=1000,null=True,blank=True)
    # ------------------------------------------
    phone_number = models.CharField(max_length=11)
    # ------------------------------------------
    profile_photo= models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    
    class Meta:
        db_table = 'auth_user'