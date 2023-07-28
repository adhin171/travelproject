from . import views
from django.urls import path

urlpatterns = [

    path('',views.contact,name='contact'),
    # path('',views.contact1,name='contact1')



]
