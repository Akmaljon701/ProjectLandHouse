from django.contrib import admin
from apis import models
from django.contrib.auth.models import Group, User

admin.site.site_title = "Land House Admin"
admin.site.site_header = "Land House"
admin.site.index_title = "Land House Admin"
admin.site.site_brand = "Land House"
admin.site.welcome_sign = "Land House"
admin.site.copyright = "Land House"

admin.site.unregister(Group)
admin.site.unregister(User)


class ObjectPhotoInline(admin.TabularInline):
    model = models.ObjectPhoto
    extra = 1


class ObjectAdmin(admin.ModelAdmin):
    inlines = [ObjectPhotoInline]
    list_display = ('title', 'status', 'created_at')
    search_fields = ('title', 'name')


admin.site.register(models.Object, ObjectAdmin)

