from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


from .models import Catagory , Product , Cart , User_detail

# Create your views here.


def get_base_context() :
    mens = Catagory.objects.filter(garment_type = 'M')
    womens = Catagory.objects.filter(garment_type = 'W')
    kids = Catagory.objects.filter(garment_type = 'K')
    all_cats = Catagory.objects.filter()

    context = { "mens" : mens , "womens" : womens , "kids" : kids , "all_cats" : all_cats  }
    return context

def get_products(tag) :
    if tag :
        return Product.objects.filter(catagory = tag)
    else :
        return Product.objects.filter()

def home(request) :
    return render(request,'home.html',get_base_context())


def productlist(request) :
    if request.method == 'GET' :
        tag = request.GET['tag']
        context = get_base_context()
        products = get_products(tag)
        context.update({ 'products' : products }) 
        return render(request , 'productlist.html' , context)
    else :
        messages.warning(request,"items not found list")
        return redirect('home')

def add_to_cart(request):
    if request.user.is_authenticated :

        if request.method == "POST" :
            productid   = request.POST.get('productid')
            quantity    = request.POST.get('quantity')
            product     = Product.objects.get( id = productid)
            user        = request.user
            
            item        = Cart( product = product , user = user , quantity = quantity )
            item.save()

            messages.success(request,"item added to cart")
            return redirect('/')

        else :
            messages.warning(request,"error")
            return redirect('/')
    else :
        messages.warning(request,"please login first")
        return redirect('/')




def productview(request):
    if request.method == 'GET' :
        id = request.GET['id']
        context = get_base_context()
        product = Product.objects.filter(id = id)
        context.update({ 'product' : product })
        return render(request , 'productview.html' , context)


    else :
        messages.warning(request,"item not found view")
        return redirect('home')

def cart(request) :
    if request.user.is_authenticated :
        if request.method == "POST" :
            
            productid = request.POST.get('productid')
            Cart.objects.filter( id = productid ).delete()

            messages.success(request,"item removed")
            return redirect('cart')

        else :
            cart_products = Cart.objects.filter(user = request.user)
            context = get_base_context()
            details = User_detail.objects.filter(user = request.user )
            context.update({ 'cart_products' : cart_products })
            context.update({'details' : details})
            return render(request , 'cart.html' , context)
    
    else :
        messages.warning(request,"please login to use cart")
        return redirect('home')

def save_user_detail(request) :
    if request.user.is_authenticated :
        if request.method == "POST" :

            full_name   = request.POST['full_name']
            phone       = request.POST['phone']
            alt_phone   = request.POST['alt_phone']
            town        = request.POST['town']
            pincode     = request.POST['pincode']
            detailid    = request.POST['detailid']

            User_detail.objects.filter(id = detailid).update( full_name = full_name , phone = phone ,
                                    alt_phone = alt_phone ,
                                    town = town , pincode = pincode )
            
            return redirect('cart')

        

        else :
            messages.warning(request,"error")
            return redirect('home')
    else :
        messages.warning(request,"error")
        return redirect('home')

def update_user_detail(request) :
    if request.user.is_authenticated :
        if request.method == "POST" :

            full_name   = request.POST['full_name']
            phone       = request.POST['phone']
            alt_phone   = request.POST['alt_phone']
            town        = request.POST['town']
            pincode     = request.POST['pincode']
            detailid    = request.POST['detailid']

            User_detail.objects.filter(id = detailid).update( full_name = full_name , phone = phone ,
                                    alt_phone = alt_phone ,
                                    town = town , pincode = pincode )
            
            return redirect('cart')

        

        else :
            messages.warning(request,"error")
            return redirect('home')
    else :
        messages.warning(request,"error")
        return redirect('home')



def signup(request) :
    if request.method == 'POST' :
        
        fname       = request.POST['fname']
        lname       = request.POST['lname']
        phone       = request.POST['phone']
        email       = request.POST['email']
        password    = request.POST['pass'] 

        customer    = User.objects.create_user(phone, email, password)
        customer.first_name = fname
        customer.last_name = lname
        customer.save()

        messages.success(request,"you have been successfully registred")
        

        return redirect('home')

    else :
        messages.denger(request,'something has gone wrong please try again or contact admin')
        return redirect('home')



def signin(request) :
    if request.method == 'POST' :
        loginusername = request.POST['loginuname']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username = loginusername , password = loginpassword)

        if user is not None :
            login(request, user)
            messages.success(request,'welcome you are ready to shop')
            return redirect('home')

        else :
            messages.warning(request,'invalid user credentials please try again')
            return redirect('home')


    return HttpResponse('404 not found')


def signout(request) :
    logout(request)
    messages.success(request,'succesfully loged out')
    return redirect('home')