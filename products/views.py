from http.client import HTTPResponse
from pydoc import render_doc
from tkinter import E
from django.shortcuts import render, redirect
from accounts.models import Profile
from products.models import Product
from django.http import HttpResponseRedirect,HttpResponse





def get_product(request , slug):
    print(request.user.profile.get_cart_count)
    try:
        product = Product.objects.get(slug =slug)
        
        unikey=Profile.objects.all()
        
        context = {'product' : product,'unikey':unikey}
        if request.GET.get('size'):
            size=request.GET.get('size')
            price=product.get_product_price_by_size(size)
            context['selected_size']=size
            context['updated_price']=price
           
            print(unikey)
            print(price)
            
        return render(request  , 'product/product.html' , context = context)

    except Exception as e:
        print(e)
          

