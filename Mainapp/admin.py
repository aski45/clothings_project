from django.contrib import admin

# Register your models here. 

from .models import Product
admin.site.register(Product)

from .models import Catagory
admin.site.register(Catagory)


from .models import Order
admin.site.register(Order)


from .models import Cart
admin.site.register(Cart)

from .models import User_detail
admin.site.register(User_detail)