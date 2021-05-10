from django.contrib import admin
from django.urls import path,include
from Mainapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home , name='home'),

    path('productlist',views.productlist, name = 'products'),
    path('productview',views.productview, name = 'Product Details'),

    path('cart',views.cart, name = 'cart'),
    path('add_to_cart',views.add_to_cart, name = 'add_to_cart'),
    path('save_user_detail',views.save_user_detail, name = 'save_user_detail'),    

    path('signup',views.signup, name = 'signup'),
    path('signin',views.signin, name = 'login'),
    path('signout',views.signout, name = 'logout'),

]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
