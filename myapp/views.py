from django.shortcuts import render,redirect
from .models import *
from django.core import serializers
# Create your views here.

def index(request):
    category = Category.objects.all()
    if 'user' in request.session:
        email = request.session['user']
        user = Register.objects.get(email=email)
        count = Cart.objects.filter(user_id=user.id).count()
        return render(request,"index.html",{'category':category,'count':count})
    count = 0
    return render(request,"index.html",{'category':category,'count':count})

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            valid = Register.objects.get(email=email)
            if valid.password==password:
                request.session['user']=email
                return redirect('index')
            else:
                return redirect('login')
        except:
            return redirect('index')
    else:
        return render(request,"login.html")
def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('login')
    return redirect('login')

def product_list(request):
    category = Category.objects.all()
    return render(request,"product_list.html",{'category':category})

def cart(request):
    if 'user' in request.session:
        email = request.session['user']
        user = Register.objects.get(email=email)
        cart = Cart.objects.filter(user_id=user.id)
        category = Category.objects.all()
        total = []
        for i in cart:
            total.append(i.price)
        total=sum(total)
        return render(request,"cart.html",{'cart':cart,'category':category,'total':total})
    else:
        return redirect('login')

def checkout(request):
    category = Category.objects.all()
    email = request.session['user']
    user = Register.objects.get(email=email)
    cart = Cart.objects.filter(user_id=user.id)
    total = []
    for i in cart:
        total.append(i.price)
    total=sum(total)
    shipping_total = total+50
    return render(request,"checkout.html",{'category':category,'user':user,'cart':cart,'total':total,'shipping_total':shipping_total})

def order(request):
    if request.method =="POST":
        Name = request.POST['Name']
        email1 = request.POST['email']
        city = request.POST['city']
        zipcode = request.POST['zipcode']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        number = request.POST['number']
        try:
            terms_condition = request.POST['selector']
            print(terms_condition)
            import random
            order_id = random.randint(0000,9999)
            email = request.session['user']
            user = Register.objects.get(email=email)
            cart = Cart.objects.filter(user_id=user.id)
            data = serializers.serialize('json',cart)
            print(data)
            if terms_condition == "on":
                Order(name=Name,email=email1,city=city,phone=number,terms_condition=True,pincode=zipcode,address1=add1,address2=add2,order_id=order_id,products=data).save()
                Cart.objects.filter(user_id=user.id).delete()
                return redirect('index')
            else:
                return redirect('checkout')
        except:
            return redirect('register')
def register(request):
    if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        if pass1 == pass2:
            obj = Register(name=name,email=email,phone=phone,password=pass1)
            obj.save()
            return redirect('index')
        else:
            return redirect('register')
    else:
        return render(request,"register.html")

def contact(request):
    category = Category.objects.all()
    return render(request,"contact.html",{'category':category})

def elements(request):
    category = Category.objects.all()
    return render(request,"elements.html",{'category':category})


def about(request):
    category = Category.objects.all()
    return render(request,"about.html",{'category':category})

def single_blog(request):
    category = Category.objects.all()
    return render(request,"single-blog.html",{'category':category})

def blog(request):
    category = Category.objects.all()
    return render(request,"blog.html",{'category':category})

def confirmation(request):
    category = Category.objects.all()
    return render(request,"confirmation.html",{'category':category})

def single_product(request,id):
    category = Category.objects.all()
    product = Product.objects.get(id=id)
    return render(request,"single-product.html",{'product':product,'category':category})

def cat(request,id):
    products = Product.objects.filter(cat_name_id=id)
    print(products)
    category = Category.objects.all()
    return render(request,"Catagori.html",{'products':products,'category':category})

def Catagory(request):
    products = Product.objects.all()
    category = Category.objects.all()
    return render(request,"Catagori.html",{'products':products,'category':category})

def add_to_cart(request,id):
    email = request.session['user']
    user = Register.objects.get(email=email)
    product = Product.objects.get(id=id)
    count = Cart.objects.filter(user_id=user.id,product_id=product.id).count()
    cart = Cart.objects.filter(user_id=user.id,product_id=product.id)
    print("####",count)
    if count>0:
        qty = cart[0].qty+1
        price = qty*product.price
        Cart.objects.filter(user_id=user.id,product_id=product.id).update(qty=qty,price=price)
        return redirect('index')
    else:
        Cart(user_id=user.id,product_id=product.id,qty=1,price=product.price).save()
        return redirect('index')


def minus(request,id):
    cart = Cart.objects.filter(id=id)
    if cart[0].qty==1:
        qty = 1
    else:
        qty = cart[0].qty-1

    price = qty * cart[0].product.price
    Cart.objects.filter(id=id).update(price=price,qty=qty)
    return redirect('cart')

def plus(request,id):
    cart = Cart.objects.filter(id=id)
    qty = cart[0].qty+1
    price = qty * cart[0].product.price
    Cart.objects.filter(id=id).update(price=price,qty=qty)
    return redirect('cart')

def delete(request,id):
    cart = Cart.objects.filter(id=id)
    cart.delete()
    return redirect('cart')