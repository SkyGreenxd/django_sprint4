from django.contrib import admin
from .models import Category, Location, Post, Comment


class PostInline(admin.StackedInline):
    model = Post
    extra = 0
    show_change_link = True


class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostInline,)
    list_display = ('title', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('is_published',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('title',)
    search_fields = ('title', 'text')
    readonly_fields = ('created_at',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
