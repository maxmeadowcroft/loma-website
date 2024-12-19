from django.contrib import admin
from .models import MoviePoster, BackgroundImage, ConcessionItem, TicketPrice

admin.site.register(MoviePoster)
admin.site.register(BackgroundImage)


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