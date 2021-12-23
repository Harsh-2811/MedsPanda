from .views import *
from django.urls import path,include

urlpatterns = [
    
    path('',index,name="Home" ),
    path('processToCheckout/<int:pk>/',processToCheckout,name="processToCheckout"),
    path('policy/',policy,name="policy" ),
    path('terms',terms,name="terms" ),
    path('contact',contact,name="contact" ),
    path('thankyou/<str:orderId>/',thankyou,name="thankyou" ),
    path('singleForm/',singleForm,name="singleForm" ),





]