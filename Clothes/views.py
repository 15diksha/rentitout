from django.shortcuts import render, redirect
from django.http import HttpResponse
from Clothes.models import Clothes
from Owner.models import Owner

from django.shortcuts import get_object_or_404

# Create your views here.
# def upload_Clothes(request):
#     Clothes_name=request.POST.get('Clothes_name','')
#     Clothes_brand=request.POST.get('Clothes_brand','')
    
#     Clothes_type=request.POST.get('Clothes_type','')
    
#     Clothes_size=request.POST.get('Clothes_size','')
#     Clothes_color=request.POST.get('Clothes_color','')
    
    
#     Clothes_uploaded_by=request.session.get('user_email')

   
#     Clothes_description=request.POST.get('Clothes_description','')
#     Clothes_price=request.POST.get('Clothes_price','')
#     Clothes_image1=request.FILES['Clothes_image1']
#     Clothes_image2=request.FILES['Clothes_image2']
#     Clothes_image3=request.FILES['Clothes_image3']

#     result_Clothes = Clothes.objects.filter(Clothes_ID=Clothes_ID)
#     result_owner = Owner.objects.filter(Owner_email=Clothes_uploaded_by)
    

#     if result_Clothes.exists():
#         if result_owner.exists():
#             Message = "This Clothes already exist!!"
#             return render(request,'Owner_Upload_Clothes.html',{'Message':Message})
        
#     else:
#         Clothes=Clothes(Clothes_name=Clothes_name,Clothes_brand=Clothes_brand,
#         Clothes_brand=Clothes_brand,Clothes_type=Clothes_type,
#         Clothes_size=Clothes_size,Clothes_color=Clothes_color,
       
#         Clothes_uploaded_by=Clothes_uploaded_by,Clothes_description=Clothes_description,
#         Clothes_price=Clothes_price,Clothes_image1=Clothes_image1,Clothes_image2=Clothes_image2,
#         Clothes_image3=Clothes_image3)
        
#         Clothes.save()
#         if result_owner.exists():
#             return redirect('/Owner/AllClothes')
        