from django.shortcuts import render, redirect
from django.http import HttpResponse
from CustomerHome.models import Customer
from RentClothes.models import RentClothes
from Owner.models import Owner

from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'RentClothes/index.html')

def SendRequest_toOwner(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    user_email = request.session.get('user_email')

    RentClothes_Date_of_Booking=request.POST.get('RentClothes_Date_of_Booking','')
    RentClothes_Date_of_Return=request.POST.get('RentClothes_Date_of_Return','')
    Total_days=request.POST.get('Total_days','')
    RentClothes_Total_amount=request.POST.get('RentClothes_Total_amount','')
    
    RentClothes_Date_of_Booking=request.POST.get('RentClothes_Date_of_Booking','')
    RentClothes_Date_of_Booking = datetime.strptime(RentClothes_Date_of_Booking, "%b. %d, %Y").date()
    RentClothes_Date_of_Return = datetime.strptime(RentClothes_Date_of_Return, "%b. %d, %Y").date()
    
    rentClothes = RentClothes(RentClothes_Date_of_Booking=RentClothes_Date_of_Booking,
    RentClothes_Date_of_Return=RentClothes_Date_of_Return,
    Total_days=Total_days,RentClothes_Total_amount=RentClothes_Total_amount)
    

    rentClothes.save()

    customer = Customer.objects.filter(customer_email=user_email)
    if customer.exists():
        return redirect("/SentRequests/")

   
    owner = Owner.objects.filter(Owner_email=user_email)
    if owner.exists():
        return redirect("/Owner/SentRequests/")

def AcceptRequest(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    user_email = request.session.get('user_email')
    id = request.GET.get('id','')
    rentClothes = RentClothes.objects.get(id=id)
    rentClothes.isAvailable= False
    rentClothes.request_responded_by = user_email
    rentClothes.request_status = "Accepted"
    rentClothes.save()

   
    
    owner = Owner.objects.filter(Owner_email=user_email)
    if owner.exists():
        return redirect("/Owner/RentRequest/")

def DeclineRequest(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    user_email = request.session.get('user_email')
    id = request.GET.get('id','')
    rentClothes = RentClothes.objects.get(id=id)
    rentClothes.isAvailable= True
    rentClothes.request_responded_by = user_email
    rentClothes.request_status = "Declined"
    rentClothes.save()
    
    
    
    owner = Owner.objects.filter(Owner_email=user_email)
    if owner.exists():
        return redirect("/Owner/RentRequest/")

def CancelRequest(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    user_email = request.session.get('user_email')
    id = request.GET.get('id','')
    rentClothes = RentClothes.objects.get(id=id)
    rentClothes.delete()

    customer = Customer.objects.filter(customer_email=user_email)
    if customer.exists():
        return redirect("/SentRequests/")

    
    owner = Owner.objects.filter(Owner_email=user_email)
    if owner.exists():
        return redirect("/Owner/SentRequests/")