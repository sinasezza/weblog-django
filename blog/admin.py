from django.contrib import admin
from . import models

class PostAdming(admin.ModelAdmin):
    list_display = ('title' , 'post_author','create_date','post_status',)

class PostImagesAdmin(admin.ModelAdmin):
    list_display = ('post' , 'id' , 'image')

class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ('post','id','user','comment','created_date','active')


admin.site.register(models.Post,PostAdming)
admin.site.register(models.PostImage,PostImagesAdmin)
admin.site.register(models.PostComment,PostCommentsAdmin)