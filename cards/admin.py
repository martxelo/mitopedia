from django.contrib import admin
from django.utils.html import mark_safe



@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ('Main', {'fields': ('name', 'tags',)}),
    #     ('Vector', {'fields': ('svg', 'svg_image')}),
    # )
    # list_display = ['name', 'svg_image_thumb', 'tags']
    # readonly_fields = ['svg_image', 'svg_image_thumb']
    # list_editable = ['tags']
    # list_filter = ['tags']
    # search_fields = ['name', 'tags__name']
    # save_on_top = True
