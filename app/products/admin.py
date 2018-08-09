from django.contrib import admin

from products.models.productinfo import \
    ProductTicketList, ProductGuideTourList, \
    ProductActivityList, Comment, \
    ProductTicketDetail, ProductGuideTourDetail, \
    ProductActivityDetail

admin.site.register(ProductTicketList)
admin.site.register(ProductGuideTourList)
admin.site.register(ProductActivityList)
admin.site.register(Comment)
admin.site.register(ProductTicketDetail)
admin.site.register(ProductGuideTourDetail)
admin.site.register(ProductActivityDetail)
# admin.site.register(TicketPriceInfo)
# admin.site.register(GuidePriceInfo)
# admin.site.register(ActivityPriceInfo)