from .views import *
from django.urls import path,include

urlpatterns = [
    
    path('',index,name="Home" ),
    path('policy/',policy,name="policy" ),
    path('terms',terms,name="terms" ),


]