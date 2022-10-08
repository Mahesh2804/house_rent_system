from house_customer import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HouseOwner, Houses
from house_customer.models import Orders, HouseCustomer
from .forms import HouseOwnerForm, HousesForm
from django.db.models import Q


def houses_ownerregister(request):
    if request.method == 'POST':
        form = HouseOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'houses_ownerlogin.html')
    else:
        form = HouseOwnerForm()
    return render(request, 'houses_ownerregister.html', {'form': form})


def houses_ownerlogin(request):
    if request.method == 'POST':
        username = request.POST["name"]
        password = request.POST["pwd"]
        flag = HouseOwner.objects.filter(Q(username__iexact=username) & Q(password__iexact=password))
        if flag:
            request.session['username'] = username
            return redirect('h_owner_home')
        else:
            return render(request,'houses_ownerloginfailed.html', {'message': 'Wrong Username / Password.'})
    else:
        return render(request, 'houses_ownerlogin.html')


def houses_ownerlogout(request):
    request.session['username'] = ""
    return render(request, 'houses_ownerlogin.html')


def h_owner_home(request):
    username = request.session["username"]
    return render(request, 'h_owner_home.html', {'username': username})

    
def h_owner_profile(request): 
    uname = request.session["username"]
    obj = HouseOwner.objects.get(username=uname)
    context = {
        'object': obj,
        'username': uname,
    }
    return render(request, "h_owner_profile.html", context)


def h_owner_requests(request): 
    uname = request.session["username"]
    count = Orders.objects.filter(owner_name=uname).count()
    orders = Orders.objects.filter(owner_name=uname)
    context = {
        'orders': orders,
        'username': uname,
        'count': count,
    }
    return render(request, "h_owner_requests.html", context)


def h_owner_add(request): 
    username = request.session["username"]
    if request.method == 'POST':
        form = HousesForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.owner_name = username
            form1.save()
            return redirect('h_owner_manage')
    else:
        form = HousesForm()
    return render(request, 'h_owner_add.html', {'form': form, 'username': username})


def h_owner_manage(request): 
    username = request.session["username"]
    houses = Houses.objects.filter(owner_name=username)  # select * from student_table
    count = Houses.objects.filter(owner_name=username).count()  # select count(*) from student_table
    return render(request, 'h_owner_manage.html', {'houses': houses, 'count': count, 'username': username})

    
def destroy(request):
    username = request.session["username"]
    if request.method == 'POST':
        doorno = request.POST['doorno']
        house = Houses.objects.get(doorno=doorno)
        house.delete()
        return redirect('h_owner_manage')

def update(request):
    username = request.session["username"]
    if request.method == 'POST':
        doorno = request.POST['doorno']
        house = Houses.objects.get(doorno=doorno)
        form = HousesForm(request.POST, instance=house)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.owner_name = username
            form1.save()
            return redirect('h_owner_manage')
        else:
            form = HousesForm()
    return render(request, 'h_owner_update.html', {'form': form, 'username': username, 'house': house})

