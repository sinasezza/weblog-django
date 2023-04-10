from django.contrib import admin
from . import models

class PostAdming(admin.ModelAdmin):
    list_display = ('title' , 'post_author','create_date','post_status',)

class PostImagesAdmin(admin.ModelAdmin):
    list_display = ('post' , 'id' , 'image')


admin.site.register(models.Post,PostAdming)
admin.site.register(models.PostImage,PostImagesAdmin)