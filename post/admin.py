from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "productdate", 'slug']
    list_display_links = ['title', 'productdate']
    list_filter = ['title']
    search_fields = ['title', 'body']


    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
