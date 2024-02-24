from django.contrib import admin
from .models import Tag, Blog, Comment, Content, BlogCommentLike


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ContentInlineAdmin(admin.StackedInline):
    model = Content
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [ContentInlineAdmin, ]
    list_display = ('id', 'title', 'modified_date', 'created_date')
    readonly_fields = ('modified_date', 'created_date')
    date_hierarchy = 'created_date'
    search_fields = ('title',)
    list_filter = ('tags', )
    filter_horizontal = ['tags']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'parent', 'created_date')
    readonly_fields = ('modified_date', 'created_date')
    date_hierarchy = 'created_date'
    search_fields = ('author',)
    autocomplete_fields = ('blog',)


@admin.register(BlogCommentLike)
class BlogCommentLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'author', )
    autocomplete_fields = ('comment', 'author', )
    search_fields = ('comment', )


# admin.site.register(BlogParentLike)
