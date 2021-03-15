from django.contrib import admin

from app.models import Audio, Video, Text, Page, ContentItemOnPage


# Content models


class ContentItemInline(admin.TabularInline):
    """
    Page content item inline control
    """
    model = ContentItemOnPage
    extra = 1


class PageAdmin(admin.ModelAdmin):
    """
    Page admin form with content items
    """
    inlines = (ContentItemInline,)
    search_fields = ('title__icontains',)


admin.site.register(Page, PageAdmin)


class AudioAdmin(admin.ModelAdmin):
    search_fields = ('title__icontains',)


admin.site.register(Audio, AudioAdmin)


class VideoAdmin(admin.ModelAdmin):
    search_fields = ('title__icontains',)


admin.site.register(Video, VideoAdmin)


class TextAdmin(admin.ModelAdmin):
    search_fields = ('title__icontains', 'content__istartswith',)


admin.site.register(Text, TextAdmin)
