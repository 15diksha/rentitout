from django.urls import path
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('UploadClothes/', views.upload_Clothes,name="UploadClothes"),
    path('Owner/',include("Owner.urls"))
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)