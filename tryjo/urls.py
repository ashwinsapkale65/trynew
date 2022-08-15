
from django.urls import path
from tryjo import views

urlpatterns = [
   
    path('',views.index,name='index.html')
]
