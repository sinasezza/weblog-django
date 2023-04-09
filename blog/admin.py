from django.contrib import admin
from . import models

class PostAdming(admin.ModelAdmin):
    list_display = ('title' , 'post_author','create_date','post_status',)


admin.site.register(models.Post,PostAdming)