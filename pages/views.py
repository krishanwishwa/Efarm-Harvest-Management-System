from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Product
from .forms import Productform
from django.contrib.auth.decorators import login_required
from django.utils import timezone



def home(request):
    return render(request, 'pages/home.html')

@login_required
def addproduct(request):
    if request.method == 'GET':
        return render(request, 'products/addproduct.html', {'form':Productform()})
    else :
        form = Productform(request.POST,request.FILES or None)
        if form.is_valid():
            newsale = form.save(commit=False)
            newsale.user = request.user
            newsale.save()
            return redirect('product')
        return render(request, 'products/addproduct.html', {'form':Productform(), 'error':'Bad data'})

def product(request):
    products = Product.objects.all()
    return render(request, 'products/product.html', {'products':products})

def productdetail(request, product_id):
    details = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()
    return render(request, 'products/product-detail.html', {'product':details,'products':products})

def contact(request):
    if request.method == "POST":
        msg_name = request.POST['name']
        msg_email = request.POST['email']
        msg_phone = request.POST['phone']
        msg_subject = request.POST['subject']
        msg_message = request.POST['message']

        #send an Email
        send_mail(
            msg_subject,
            msg_name,
            msg_message,
            # msg_phone,
            # msg_email,
            ['wdarshana784@gmail.com'] #To Email
            )

        return render(request, 'pages/contact.html',{'msg_name': msg_name})

    else:
        return render(request, 'pages/contact.html')
