from django.contrib import admin
from .models import Post, Comment, Otzivlar, Natijalar

class CommentInline(admin.TabularInline):
    model = Comment 
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Post, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Otzivlar)
admin.site.register(Natijalar)
