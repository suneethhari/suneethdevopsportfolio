
from django.urls import path
from . import views
app_name='portfolioapp'

urlpatterns = [
path('',views.demo,name='demo'),
path('single/',views.single,name='single'),
path('contact_form/',views.contact_form,name='contact_form')
]
