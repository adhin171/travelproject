
from django.shortcuts import render

from .models import place
from .models import people



# Create your views here.
# def home(request):
#     return render(request, 'home.html')

def contact(request):
    obj=place.objects.all()
    obj1 = people.objects.all()
    return render(request,'index.html',{'result':obj,'hello':obj1})

# def contact1(request):
#     obj1=people.objects.all()
#     return render(request,'index.html',{})


# def about(request):
#     return HttpResponse('about')



# def details(request):
#     return HttpResponse('details')
#
# def thanks(request):
#     return render(request,'thanks.html')
