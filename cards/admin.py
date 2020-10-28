from django.contrib import admin
from django.utils.html import mark_safe

from django.contrib.auth.models import User, Group

from cards.models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'card_type', '_eras',
                    'mythology', 'cost', 'strength',
                    'max_pow', '_tags', '_abilities',
                    'passive_effect', 'quote']
    search_fields = ['name', 'tags__name', 'abilities__name', 'passive_effect']
    list_filter = ['eras', 'card_type', 'mythology', 'abilities__phase', 'tags']
    change_list_template = "admin/change_list_filter_confirm_sidebar.html"
    fieldsets = ((
        'Card description', {
            'fields':(
                'name',
                'eras',
                'mythology',
                'tags',
                'cost',
                'strength',
                'max_pow',
                'init_pow',
                'passive_effect',
                'abilities',
                'quote',
            )
        }
    ),)
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
