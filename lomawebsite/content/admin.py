from django.contrib import admin
from .models import BackgroundImage, ConcessionItem, TicketPrice, Movie

admin.site.register(BackgroundImage)
admin.site.register(Movie)


@admin.register(ConcessionItem)
class ConcessionItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(TicketPrice)
class TicketPriceAdmin(admin.ModelAdmin):
    list_display = ('category', 'showtime', 'age_group', 'price')
    list_filter = ('category', 'showtime')
    search_fields = ('age_group',)
