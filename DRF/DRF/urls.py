from django.contrib import admin
from django.urls import path,include
from csv_to_database import views as cv

urlpatterns = [
   path('admin/', admin.site.urls),
   #path()  
   path('api-auth/', include('rest_framework.urls')),
   path('', include('accounts.urls')),
   path('api-auth/', include('drf_social_oauth2.urls',namespace='drf')),
   path('api/auth/', include('djoser.urls.authtoken')), 
   path('csv/',cv.csv_to_date),
  # path('calender/', include('testdata.urls')),

   
]