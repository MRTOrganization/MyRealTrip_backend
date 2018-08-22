from django.contrib import admin

from products.models import PopularCity
from products.models.productinfo import Product, ProductDetail

admin.site.register(PopularCity)

admin.site.register(Product)
admin.site.register(ProductDetail)
# admin.site.register(Comment)
# admin.site.register(ProductTicketDetail)
# admin.site.register(ProductGuideTourDetail)
# admin.site.register(ProductActivityDetail)
# # admin.site.register(TicketPriceInfo)
# # admin.site.register(GuidePriceInfo)
# # admin.site.register(ActivityPriceInfo)