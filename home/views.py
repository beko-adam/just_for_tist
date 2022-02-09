from multiprocessing import context
from django.shortcuts import render
from .form import CUs_form
from django.views.decorators.csrf import csrf_exempt# Create your views here.
from .models import Customer, Order, Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...


def all_older(request):
    
    if request.method == 'POST':
    
        form_Apply = CUs_form(request.POST, request.FILES)
        if form_Apply.is_valid():
            form = form_Apply.save(commit=False)
            form.save()
        print('done')

    else:

        form_Apply = CUs_form()



    return render(request,  './pags/first.html',  {'form': form_Apply})


@csrf_exempt
def creat_(request):

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    print(name, phone, email)
    Customer.objects.create(name=name, phone=phone, email=email)

    #user = User.objects.create_user(str(name), 'lennon@thebeatles.com', str(phone))
    #user.last_name = str(email)
   # user.save()
    return render(request,  './pags/creat.html',  {})



@csrf_exempt
def creat_Por(request):

    single_pro = Product.objects.get(id=1)
    all_ = Customer.objects.all()
    all__ = Product.objects.all()

    # cust = all_.customer.name
    # here get theos three values from the froms of templale 
    # the name sheld be seme name in the template and the POST>get('here')
    customer = request.POST.get('customer')
    product = request.POST.get('product')
    status = request.POST.get('status')

    print(all_, all__)

    context = {

        'Cust':all_,
        'Por': all__ ,
        'single_por' : single_pro   
        
            }

   

    Order.objects.create(customer=customer, product=product, status=status)
    return render(request,  './pags/order.html',  context)
