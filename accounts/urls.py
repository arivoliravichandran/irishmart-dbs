from django.urls import path
from accounts.models import Cart
from accounts.views import login_page,register_page , activate_email,add_to_cart,cart,remove_cart_item,logout


urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('logout/', logout, name="logout"),
   path('register/' , register_page , name="register"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('cart/' , cart , name="cart"),
   path('add-to-cart/<id>/' , add_to_cart , name="add_to_cart"),
   path('remove-from-cart/<cart_item_id>/' , remove_cart_item , name="remove_cart_item"),
]
