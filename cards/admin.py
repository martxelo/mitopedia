from django.contrib import admin
from django.utils.html import mark_safe

from django.contrib.auth.models import User, Group

from cards.models import Card
from cards import filters

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'card_type', '_eras',
                    'mythology', 'cost', 'strength',
                    'max_pow', '_tags', '_abilities',
                    'passive_effect', 'quote', 'image']
    search_fields = (
        'name', 'tags__name', 'abilities__name', 'passive_effect'
    )
    list_filter = (
        ('eras__name', filters.EraFilter),
        ('card_type', filters.CardTypeFilter),
        ('mythology__name', filters.MythologyFilter),
        ('abilities__phase', filters.AbilityFilter),
        ('tags__name', filters.TagFilter),
    )
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.unregister(User)
admin.site.unregister(Group)
