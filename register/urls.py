
from django.urls import path
from .views import RegistrationView

urlpatterns = [
   
    # path("",include("register.urls"))
    path("",RegistrationView.as_view())
]
