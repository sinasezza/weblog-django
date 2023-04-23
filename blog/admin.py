from django.contrib import admin
from . import models

 
class PostParagraphInline(admin.StackedInline):
    model = models.PostParagraph
    extra = 1
    
class PostCommentInline(admin.StackedInline):
    model = models.PostComment
    extra = 0
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title' ,'post_slug', 'post_author','create_date','post_status',)
    inlines = [PostParagraphInline,PostCommentInline]

class PostParagraphsAdmin(admin.ModelAdmin):
    list_display = ('post' , 'id' , 'order','content')
    

class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ('post','id','user','comment','created_date','active')


admin.site.register(models.Post,PostAdmin)
admin.site.register(models.PostParagraph,PostParagraphsAdmin)
admin.site.register(models.PostComment,PostCommentsAdmin)