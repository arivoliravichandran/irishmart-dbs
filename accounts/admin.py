from django.contrib import admin

# Register your models here.
from .models import Profile, Cart, CartItem

admin.site.register(Profile)

admin.site.register(Cart)

admin.site.register(CartItem)
