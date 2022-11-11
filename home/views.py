from multiprocessing import context
from django.shortcuts import render
from products.models import Product
from django.shortcuts import redirect
# Create your views here.
def index(request):
    
   


    if request.user.is_authenticated:
        context={'products':Product.objects.all()}
        return render(request , 'home/index.html',context )
    else:
        return redirect('accounts/login/')