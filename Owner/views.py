import os
from datetime import date, datetime

import matplotlib
from CustomerHome.models import Customer
from django.http import HttpResponse
from django.shortcuts import redirect, render
from matplotlib import pyplot as plt
from Owner.models import Owner
from RentClothes.models import RentClothes
from Clothes.models import Clothes

from ClothesRentingSystem.settings import MEDIA_ROOT

matplotlib.use('Agg')
import base64
import io


#Create your views here.
def index(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    Clothes = Clothes.objects.all()
    Message="Welcome Aboard!!"
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_index.html',{'Clothes':Clothes,'Message':Message,'owner':owner,'no_of_pending_request':no_of_pending_request})

def Profile(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_Profile.html',{'owner':owner,'no_of_pending_request':no_of_pending_request})

# def register_manager(request):
#     if('user_email' not in request.session):
#         return redirect('/signin/')
#     owner_email = request.session.get('user_email')
#     owner = Owner.objects.get(Owner_email=owner_email)
#     no_of_pending_request=count_pending_rent_request()
#     return render(request,'register_manager.html',{'owner':owner,'no_of_pending_request':no_of_pending_request})



    # result_customer = Customer.objects.filter(customer_email=Manager_email)
    # result_owner = Owner.objects.filter(Owner_email=Manager_email)
   
    # if result_customer.exists() or result_owner.exists() :
    #     Message = "This Email address already exist!!"
    #     return render(request,'register_manager.html',{'Message':Message})

       



def AllCustomers(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    customer = Customer.objects.all()
    no_of_pending_request=count_pending_rent_request()
    return render(request,"All_Customers.html",{'customer':customer,'owner':owner,'no_of_pending_request':no_of_pending_request})



def Customer_Profile(request,customer_email):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    customer = Customer.objects.get(customer_email=customer_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_Customer_Profile.html',{'owner':owner,'customer':customer,'no_of_pending_request':no_of_pending_request})

# def upload_Clothes(request):
#     if('user_email' not in request.session):
#         return redirect('/signin/')
#     owner_email = request.session.get('user_email')
#     owner = Owner.objects.get(Owner_email=owner_email)
#     no_of_pending_request=count_pending_rent_request()
#     return render(request,"Owner_Upload_Clothes.html",{'owner':owner,'no_of_pending_request':no_of_pending_request})

def AllClothes(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    Clothes = Clothes.objects.all()
    no_of_pending_request=count_pending_rent_request()
    return render(request,"Owner_all_Clothes.html",{'Clothes':Clothes,'owner':owner,'no_of_pending_request':no_of_pending_request})

def showdetails(request,Clothes_id):
    if('user_email' not in request.session):
        return redirect('/signin/')
    Clothes = Clothes.objects.get(Clothes_id=Clothes_id)
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_showdetails.html',{'Clothes':Clothes,'owner':owner,'no_of_pending_request':no_of_pending_request})

def CheckAvailability(request,Clothes_id):
    if('user_email' not in request.session):
        return redirect('/signin/')

    RentClothes_Date_of_Booking=request.POST.get('RentClothes_Date_of_Booking','')
    RentClothes_Date_of_Return=request.POST.get('RentClothes_Date_of_Return','')
    print(RentClothes_Date_of_Booking)
    RentClothes_Date_of_Booking = datetime.strptime(RentClothes_Date_of_Booking, '%Y-%m-%d').date()
    print(RentClothes_Date_of_Booking)
    RentClothes_Date_of_Return = datetime.strptime(RentClothes_Date_of_Return, '%Y-%m-%d').date()

    rentClothes = RentClothes.objects.filter(Clothes_id=Clothes_id)
    Clothes = Clothes.objects.get(Clothes_id=Clothes_id)

    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)

    no_of_pending_request=count_pending_rent_request()

    if RentClothes_Date_of_Booking < date.today():
        Incorrect_dates = "Please give proper dates"
        return render(request,'Owner_showdetails.html',{'Incorrect_dates':Incorrect_dates,'Clothes':Clothes,'owner':owner,'no_of_pending_request':no_of_pending_request})

    if RentClothes_Date_of_Return < RentClothes_Date_of_Booking:
        Incorrect_dates = "Please give proper dates"
        return render(request,'Owner_showdetails.html',{'Incorrect_dates':Incorrect_dates,'Clothes':Clothes,'owner':owner,'no_of_pending_request':no_of_pending_request})
    
    days=(RentClothes_Date_of_Return-RentClothes_Date_of_Booking).days+1
    total=days*Clothes.Clothes_price
    
    rent_data = {"RentClothes_Date_of_Booking":RentClothes_Date_of_Booking, "RentClothes_Date_of_Return":RentClothes_Date_of_Return,"days":days, "total":total}
    
    for rv in rentClothes:

        
        if (rv.RentClothes_Date_of_Booking >= RentClothes_Date_of_Booking and RentClothes_Date_of_Return >= rv.RentClothes_Date_of_Booking) or (RentClothes_Date_of_Booking >= rv.RentClothes_Date_of_Booking and RentClothes_Date_of_Return <= rv.RentClothes_Date_of_Return) or (RentClothes_Date_of_Booking <= rv.RentClothes_Date_of_Return and RentClothes_Date_of_Return >= rv.RentClothes_Date_of_Return):
            if rv.isAvailable:
                Available = True
                Message = "Note that somebody has also requested for this Clothes from " + str(rv.RentClothes_Date_of_Booking) + " to " + str(rv.RentClothes_Date_of_Return)
                return render(request,'Owner_showdetails.html',{'Message':Message,'Available':Available,'Clothes':Clothes,'owner':owner,'rent_data':rent_data,'no_of_pending_request':no_of_pending_request})

            NotAvailable = True
            return render(request,'Owner_showdetails.html',{'NotAvailable':NotAvailable,'dates':rv,'Clothes':Clothes,'owner':owner,'no_of_pending_request':no_of_pending_request})
    
    Available = True
    return render(request,'Owner_showdetails.html',{'Available':Available,'Clothes':Clothes,'owner':owner,'rent_data':rent_data,'no_of_pending_request':no_of_pending_request})

def RentRequest(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)

    rentClothes = RentClothes.objects.all()
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_RentRequest.html',{'owner':owner,'rentClothes':rentClothes,'no_of_pending_request':no_of_pending_request})

def SentRequests(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)

    no_of_pending_request=count_pending_rent_request()

    rentClothes = RentClothes.objects.filter(customer_email=owner_email)
    if rentClothes.exists():
        Clothes = Clothes.objects.all()
        return render(request,'Owner_SentRequests.html',{'owner':owner,'rentClothes':rentClothes,'Clothes':Clothes,'no_of_pending_request':no_of_pending_request})
    else:
        Message = "You haven't rented any Clothes yet!!"
        return render(request,'Owner_SentRequests.html',{'owner':owner,'rentClothes':rentClothes,'Message':Message,'no_of_pending_request':no_of_pending_request})


def DeleteClothes(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

   

    path1 = MEDIA_ROOT + str(Clothes.Clothes_image1)
    path2 = MEDIA_ROOT + str(Clothes.Clothes_image2)
    path3 = MEDIA_ROOT + str(Clothes.Clothes_image3)

    os.remove(path1)
    os.remove(path2)
    os.remove(path3)

    Clothes.delete()
    

    return redirect('/Owner/AllClothes/')

def count_pending_rent_request():
    no_of_pending_request=0
    rentClothes = RentClothes.objects.all()
    for rv in rentClothes:
        if rv.request_status == "Pending":
            no_of_pending_request+=1
    return no_of_pending_request

def customer_gender_chart():
    customer = Customer.objects.all()
    fig = plt.figure(figsize =(10, 7))
    male_counter = 0
    female_counter = 0
    other = 0
    for cust in customer:
        if cust.customer_gender == 'Male':
            male_counter += 1
        elif cust.customer_gender == 'Female':
            female_counter += 1
        else:
            other += 1
    gender = ['Male','Female', 'Other']
    data = [male_counter, female_counter, other]

    plt.pie(data, labels = gender, autopct='%1.1f%%', startangle=90)
    flike = io.BytesIO()
    fig.savefig(flike)
    cust_gender = base64.b64encode(flike.getvalue()).decode()
    return cust_gender

def customer_no_of_rent_request():
    cust_dict = {}
    rentClothes = RentClothes.objects.all()
    for rv in rentClothes:
        if rv.customer_email not in cust_dict.keys():
            cust_dict[rv.customer_email] = 1
        else:
            cust_dict[rv.customer_email] += 1
    cust_email = list(cust_dict.keys())
    cust_no_of_rent_request = list(cust_dict.values())
    fig = plt.figure(figsize = (12, 6))
 
    #creating the bar plot
    plt.bar(cust_email, cust_no_of_rent_request, color ='green',
            width = 0.4)
    plt.xticks(cust_email, cust_email, rotation=10, horizontalalignment='right')
    plt.xlabel("Customer Email")
    plt.ylabel("No. of Rent Requests")
    plt.show()
    flike = io.BytesIO()
    fig.savefig(flike)
    cust_no_of_rent_request = base64.b64encode(flike.getvalue()).decode()
    return cust_no_of_rent_request

def Clothes_type_chart():
    Clothes = Clothes.objects.all()
    fig = plt.figure(figsize =(10, 7))
    women_ethnic_sets, women_western_wear,women_formal, men_ethnic_wear, men_casual, men_formal,other = 0, 0, 0, 0, 0, 0, 0
    for v in Clothes:
        if v.Clothes_type == 'women_ethnic_sets':
            women_ethnic_sets += 1
        elif v.Clothes_type == 'women_western_wear':
            women_western_wear += 1
        elif v.Clothes_type == 'women_formal':
            women_formal+= 1
        elif v.Clothes_type == 'men_ethnic_wear':
            men_ethnic_wear += 1
        elif v.Clothes_type == 'men_casual':
            men_casual += 1
        elif v.Clothes_type == 'men_formal':
            men_formal += 1
        else:
            other += 1
    type = ['women_ethnic_sets','women_western_wear', 'women_formal', 'men_ethnic_wear', 'men_casual', 'men_formal', 'Other']
    data = [women_ethnic_sets, women_western_wear, women_formal, men_ethnic_wear, men_casual, men_formal, other]

    plt.pie(data, labels = type, autopct='%1.1f%%', startangle=90)
    flike = io.BytesIO()
    fig.savefig(flike)
    v_type = base64.b64encode(flike.getvalue()).decode()
    return v_type

def Clothes_no_of_rent_request():
    clothes_dict = {}
    rentClothes = RentClothes.objects.all()
    for rv in rentClothes:
        if rv.Clothes_id not in clothes_dict.keys():
            clothes_dict[rv.Clothes_id] = 1
        else:
            clothes_dict[rv.Clothes_id] += 1
    v_id = list(clothes_dict.keys())
    v_no_of_rent_request = list(clothes_dict.values())
    fig = plt.figure(figsize = (12, 6))
 
    #creating the bar plot
    plt.bar(v_id, v_no_of_rent_request, color ='maroon',
            width = 0.4)
    plt.xticks(v_id, v_id, rotation=10, horizontalalignment='right')
    plt.xlabel("Clothes Id")
    plt.ylabel("No. of Rent Requests")
    plt.show()
    flike = io.BytesIO()
    fig.savefig(flike)
    v_no_of_rent_request = base64.b64encode(flike.getvalue()).decode()
    return v_no_of_rent_request

def ViewAnalysis(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)

    no_of_pending_request=count_pending_rent_request()
    cust_gender = customer_gender_chart()
    cust_no_of_rent_request = customer_no_of_rent_request()
    v_type = Clothes_type_chart
    v_no_of_rent_request = Clothes_no_of_rent_request()
    
    return render(request, 'Analysis.html', {'owner':owner, 'no_of_pending_request':no_of_pending_request,'cust_gender':cust_gender, 'cust_rent_request':cust_no_of_rent_request, 'v_type':v_type, 'v_rent_request':v_no_of_rent_request})