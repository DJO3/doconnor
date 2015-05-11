from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from blog import models


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}  # adds markdown widets to admin


class EduOrgAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
admin.site.register(models.EduOrg, EduOrgAdmin)
admin.site.register(models.Course)
