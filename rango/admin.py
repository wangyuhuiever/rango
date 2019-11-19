from django.contrib import admin
from rango.models import Category, Page


class PageInLine(admin.StackedInline):
    model = Page
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    inlines = [PageInLine]


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
