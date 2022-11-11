from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
from products.models import Product,SizeVariant
from accounts.models import Cart,CartItem
from django.contrib.auth import logout
from django.contrib.auth import logout as django_logout


# Create your views here.
from .models import Profile


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username = email)

            if not user_obj.exists():
                messages.warning(request, 'Account not found.')
                return HttpResponseRedirect(request.path_info)


            if not user_obj[0].profile.is_email_verified:
                messages.warning(request, 'Your account is not verified.')
                return HttpResponseRedirect(request.path_info)

            user_obj = authenticate(username = email , password= password)
            if user_obj:
                login(request , user_obj)
                return redirect('/')

            

            messages.warning(request, 'Invalid credentials')
            return HttpResponseRedirect(request.path_info)


        return render(request ,'accounts/login.html')


def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')




def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')


def add_to_cart(request,id):
    variant=request.GET.get('variant')
    product=Product.objects.get(id=id)
    user=request.user
    cart , _ = Cart.objects.get_or_create(user=user,is_paid=False)
    cart_item  = CartItem.objects.create(cart=cart,product=product,)

    if variant:
        variant=request.GET.get('variant')
        size_variant=SizeVariant.objects.get(size_name=variant)
        cart_item.size_variant=size_variant
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_cart_item(request,id):
    try:
        cart_item=CartItem.objects.get(id=id)
        cart_item.delete()
        
    except Exception as e:
        print(e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart(request):
    user=request.user
    cart , _ = Cart.objects.get_or_create(user=user,is_paid=False)
    cart_items=CartItem.objects.filter(cart=cart)
    
    context={'cart_items':cart_items}
    return render(request,'home/cart.html',context)

def logout(request):
    django_logout(request)
    return redirect('/')