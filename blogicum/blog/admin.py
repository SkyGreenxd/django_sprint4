from django.contrib import admin
from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'slug')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published')
    list_filter = ('category', 'location')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)

class PostInline(admin.StackedInline):
    model = Post
    extra = 0
    show_change_link = True


admin.site.register(Post)
admin.site.register(Location)
admin.site.register(Category)
