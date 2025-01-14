from django.urls import path
from . import views

urlpatterns = [
    
    
    path('landing', views.landing, name='landing_page'),
    path('',views.note,name="notes")  # Landing page


]