from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HouseCustomer
from .forms import HouseCustomerForm, SearchForm
from django.db.models import Q
from house_owner.models import Houses, HouseOwner
from house_customer.models import Orders
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def houses_customerregister(request):
    if request.method == 'POST':
        form = HouseCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'houses_customerlogin.html')
    else:
        form = HouseCustomerForm()
    return render(request,'houses_customerregister.html',{'form':form})


def houses_customerlogin(request):
    if request.method == 'POST':
        username = request.POST["name"]
        password = request.POST["pwd"]
        flag = HouseCustomer.objects.filter(Q(username__iexact=username) & Q(password__iexact=password))
        if flag:
            request.session['username'] = username
            return redirect('h_customer_home')
        else:
            return render(request,'houses_customerloginfailed.html', {'message': 'Wrong Username / Password.'})
    else:
        return render(request,'houses_customerlogin.html')


def houses_customerlogout(request):
    request.session['username'] = ""
    return render(request, 'houses_customerlogin.html')


def h_customer_home(request):
    username = request.session["username"]
    all_houses = Houses.objects.all()
    return render(request, 'h_customer_home.html', {'username': username, 'all_houses': all_houses})


def h_customer_profile(request): 
    uname = request.session["username"]
    obj = HouseCustomer.objects.get(username=uname)
    context = {
        'object': obj,
        'username': uname,
    }
    return render(request, "h_customer_profile.html", context)
    
  
def h_customer_search(request):
    return render(request, 'h_search.html', {})
    

def h_customer_searchresults(request):
    username = request.session["username"]
    if request.method == "POST":
        # category = request.POST["category"]
        type = request.POST["type"]
        bedrooms = request.POST["bedrooms"]
        city = request.POST["city"]
        houses = Houses.objects.filter(type=type,bed_rooms=bedrooms,city=city)
        count = Houses.objects.filter(type=type,bed_rooms=bedrooms,city=city).count()
        return render(request, 'search_results.html', {'houses': houses, 'count': count, 'username': username})
    else:
        return render(request, 'h_search.html')


def h_customer_renthouse(request):
    username = request.session["username"]
    if request.method == 'POST':
        doorno = request.POST['doorno']
        owner_name = request.POST['owner_name']
        houses = Houses.objects.filter(doorno=doorno,owner_name=owner_name)
        owner = HouseOwner.objects.filter(fullname=owner_name)
        count = Houses.objects.filter(doorno=doorno,owner_name=owner_name).count()
        mylist = zip(houses, owner)
        return render(request, 'h_rent_proceed.html', {'mylist': mylist , 'count': count, 'username': username})
    else:
        return render(request, 'h_customer_home.html')


def h_customer_request(request):
    #return HttpResponse(request.POST['doorno'] + " " + request.POST['owner_name'] + " " + request.POST['customer_name'] + " " + request.POST['months'])
    username = request.session["username"]
    if request.method == 'POST':
        doorno = request.POST['doorno']
        owner_name = request.POST['owner_name']
        house = Houses.objects.filter(doorno=doorno,owner_name=owner_name)
        owner = HouseOwner.objects.filter(fullname=owner_name)
        mylist = zip(house, owner)
        return render(request, 'confirmation.html', {'mylist':mylist, 'username': username})
        

def h_confirm(request):
    username = request.session["username"]
    if request.method == 'POST':
        doorno = request.POST['doorno']
        owner_name = request.POST['owner_name']
        houses = Houses.objects.filter(doorno=doorno,owner_name=owner_name)
        owners = HouseOwner.objects.filter(fullname=owner_name)
        customers = HouseCustomer.objects.filter(fullname = username)
        mylist = zip(houses, owners, customers)
        
        for house, owner, customer in mylist:
            if house.is_available == True:
                try:
                    order = Orders()
                    order.customer_name = username
                    order.house_type = house.type
                    order.address = house.doorno + ", " + house.location + ", " + house.city
                    order.area = house.area
                    order.bedrooms = house.bed_rooms
                    order.owner_name = house.owner_name
                    order.owner_mobile = owner.mobileno
                    order.rent = house.rent
                    order.save()

                    h_owner_email = owner.email
                    h_customer_email = customer.email

                except:
                    order = Orders.objects.get(customer_name = username, house_type = house.type, adress = house.doorno + ", " + house.location + ", " + house.city, area = house.area, bedrooms = house.bedrooms, owner_name = house.owner_name, owner_mobile = owner.mobileno, rent = house.rent)
                house.is_available = False
                house.save()

                #SENDING CONFIRMATION MAIL
                c_message = "ORDER PLACED !!!\nHello {},\n\nYour order is confirmed !!! Thank you for choosing us and being a part of our journey.\n\n\nOrder Details are:\n------------------\nHouse type:\t{}\nAddress:\t{}\nArea(sq.mts):\t{}\nBedrooms:\t{}\nOwner Name:\t{}\nOwner Mobile:\t{}\nOwner Email:\t{}\nRent(Rs.)/month:\t{}".format(username, order.house_type, order.address, order.area, order.bedrooms, order.owner_name, order.owner_mobile, h_owner_email, order.rent)
                o_message = "NEW CUSTOMER ORDER !!!\nYou received an order from {}.\n\n\nOrder Details are:\n------------------\nCustomer Name:\t{}\nCustomer Mobile:\t{}\nCustomer Email:\t{}\nHouse Type:\t{}\nAddress:\t{}\nRent(Rs.)/month:\t{}".format(username, customer.fullname, customer.mobileno, h_customer_email, order.house_type, order.address, order.rent)
                send_mail("Order Confirmation", c_message, settings.EMAIL_HOST_USER, [h_customer_email]) # To Customer
                send_mail("Order Confirmation", o_message, settings.EMAIL_HOST_USER, [h_owner_email]) # To Owner

                return render(request, 'confirm.html', {'mylist':mylist, 'order': order, 'username': username})
        else:
            return render(request, 'order_failed.html')


def houses_customerbookings(request):
    username = request.session["username"]
    count = Orders.objects.filter(customer_name=username).count()
    orders = Orders.objects.filter(customer_name=username)
    return render(request, 'h_customer_bookings.html', {'username': username, 'orders':orders, 'count': count})

