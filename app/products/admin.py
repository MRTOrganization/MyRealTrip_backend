from django.contrib import admin

from products.models import PopularCity
from products.models.productinfo import \
    ProductList, Comment, \
    ProductTicketDetail, ProductGuideTourDetail, \
    ProductActivityDetail

admin.site.register(PopularCity)

admin.site.register(ProductList)
# admin.site.register(Comment)
# admin.site.register(ProductTicketDetail)
# admin.site.register(ProductGuideTourDetail)
# admin.site.register(ProductActivityDetail)
# # admin.site.register(TicketPriceInfo)
# # admin.site.register(GuidePriceInfo)
# # admin.site.register(ActivityPriceInfo)