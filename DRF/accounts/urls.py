from django.urls import path
from .views import CreateAccount,AllUsers,CurrentUser,home_view
app_name = 'users'
urlpatterns = [
   path('',home_view),
   path('create/', CreateAccount.as_view(), name="create_user"),
   path('all/', AllUsers.as_view(), name="all"),
   path('currentUser/', CurrentUser.as_view(), name="current"),
]



