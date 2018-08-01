from django.contrib import admin

from products.models.productinfo import TicketInfo, GuideTourInfo, ActivityInfo, Comment, TicketPriceInfo, \
    GuidePriceInfo, ActivityPriceInfo

admin.site.register(TicketInfo)
admin.site.register(GuideTourInfo)
admin.site.register(ActivityInfo)
admin.site.register(Comment)
admin.site.register(TicketPriceInfo)
admin.site.register(GuidePriceInfo)
admin.site.register(ActivityPriceInfo)