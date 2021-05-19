from django.contrib import admin
from django.urls import path,include


urlpatterns = [
   path('admin/', admin.site.urls),
   #path()  
   path('api-auth/', include('rest_framework.urls')),
   path('', include('accounts.urls')),
   path('api-auth/', include('drf_social_oauth2.urls',namespace='drf')),
   path('api/auth/', include('djoser.urls.authtoken')), 
  # path('calender/', include('testdata.urls')),
   
]