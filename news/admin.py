from django.contrib import admin
from .models import NewsPost, Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(NewsPost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('post_title', 'slug', 'created_on')
    search_fields = ['post_title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('post_title',)}
    summernote_fields = ('content',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'tag_name',
    )


admin.site.register(Category, CategoryAdmin)
