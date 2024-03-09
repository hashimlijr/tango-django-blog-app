from django.contrib import admin
from .models import Author, Post, Category, Comment, PostView 
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # Fields that are read-only for non-superusers
    readonly_fields = ('overview', 'content')

    # Override the get_readonly_fields method to make fields editable for superusers
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return self.readonly_fields

admin.site.register(Post, PostAdmin)

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostView)