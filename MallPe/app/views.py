
from django.shortcuts import render,redirect
from .models import Customer,Cart,Product,OrderPlaced
from django.views import View
from .forms import CustomerRegistrationForm,Customer, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



def HomeProduct(request):
    
    topwears = Product.objects.filter(category = 'TW')
    bottomwears = Product.objects.filter(category = 'BW')
    mobiles = Product.objects.filter(category = 'M')
    

    return render(request,'app/home.html',{
        'topwears':topwears,
        'bottomwears':bottomwears,
        'mobiles':mobiles,
    })

# @method_decorator(login_required,name='dispatch')
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})


#This is logic for saving the data into database
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    Cart(user_cart = user,product_cart = product).save()
    return redirect('/cart')


#This is for viewing info when url is been hit
@login_required
def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user_cart=user)
        return render(request, 'app/addtocart.html',{'carts':cart})

        


@login_required
def buy_now(request):
 return render(request, 'app/buynow.html')


@login_required
def profile(request):
 return render(request, 'app/profile.html')


@login_required
def address(request):
    address = Customer.objects.filter(user_customer=request.user)
    return render(request, 'app/address.html',{'address':address,'active':'btn-primary'})


@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user_OrderPlaced = request.user)
    return render(request, 'app/orders.html',{'op':op})


def mobile(request,data = None):
    if data == None:
        mobiles = Product.objects.filter(category = 'M')
    elif data =='Samsung' or data =='Oppo' or data =='Micromax':
        mobiles = Product.objects.filter(category = 'M').filter(brand = data)
    elif data =='below':
        mobiles = Product.objects.filter(category = 'M').filter(discounted_price__lt=10000)
    elif data =='above':
        mobiles = Product.objects.filter(category = 'M').filter(discounted_price__gt=10000)

    return render(request, 'app/mobile.html',{'mobiles':mobiles})

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congrats,Registered successfully !!')
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})



@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user_customer = user)
    amt = 0
    shipping_amt = 50
    
    return render(request, 'app/checkout.html',{'add':add,'finalamt':amt+shipping_amt})

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user_customer=usr,name = name,locality=locality,city=city,state=state,zipcode = zipcode)
            messages.success(request,'Congrats,Profile Updated successfully !!')
            reg.save()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
 


        

