from django.contrib import admin
from . models import Register,Product,Order,Category,Details,Testimonials
# Register your models here.

admin.site.register(Register)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Details)
admin.site.register(Testimonials)
