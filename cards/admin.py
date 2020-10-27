from django.contrib import admin
from django.utils.html import mark_safe

from django.contrib.auth.models import User, Group

from cards.models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'mythology']
    search_fields = ['name', 'tags__name']
    list_filter = ['eras', 'mythology', 'tags']
    fieldsets = (
        ('General', {'fields': ('name', 'tags',)}),
        ('Específico', {'fields': ('eras', 'mythology')}),
    )
    # readonly_fields = ['svg_image', 'svg_image_thumb']
    # list_editable = ['tags']
    # save_on_top = True

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.unregister(User)
admin.site.unregister(Group)
