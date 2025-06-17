from django.contrib import admin
from .models import Post , Author , Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    list_filter = ('author','tags','Date',)
    list_display = ('title' , 'Date' , 'author',)

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)