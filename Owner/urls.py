from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from CustomerHome import views as cust_views
from Clothes import views as pro_views

urlpatterns = [
    path('', views.index, name="Owner"),
    path('signin/',cust_views.signin, name="SignIn"),
    path('Logout/',cust_views.Logout, name="Logout"),
    path('Profile/',views.Profile, name="Profile"),
    # path('UploadClothes/',views.upload_Clothes, name="UploadClothes"),
   
    path('AllCustomers/',views.AllCustomers, name="AllCustomers"),
    path('AllClothes/',views.AllClothes, name="AllClothes"),
    # path('ClothesDetails/<str:Clothes_license_plate>/',views.showdetails,name="OwnerClothesDetails"),
    # path('CheckAvailability/<str:Clothes_license_plate>/',views.CheckAvailability,name="OwnerCheckAvailability"),
    path('RentRequest/',views.RentRequest,name="RentRequest"),
    path('SentRequests/',views.SentRequests,name="SentRequests"),
    
    path('DeleteClothes/',views.DeleteClothes,name="DeleteClothes"),
   
    path('CustomerProfile/<str:customer_email>/',views.Customer_Profile,name="CustomerProfile"),
    # path('Clothes/UploadClothes',pro_views.upload_Clothes,name="UploadClothes"),
    path('ViewAnalysis/',views.ViewAnalysis, name="ViewAnalysis"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)