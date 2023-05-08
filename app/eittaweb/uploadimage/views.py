from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def uploadImageViews(request):
    return render(request, 'index.html')


def uploadData(request):
    if request.method == 'POST' and request.FILES['image']:
        print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
        for f in request.FILES.getlist('image'):
            print(type(f))
            print(request.POST.get('name'))
            print(request.POST.get('number'))
            
            postmodel = UploadImageModel()

            postmodel.name = request.POST.get('name')
            postmodel.number = request.POST.get('number')
            postmodel.image = f
            postmodel.save()

            return redirect(reverse('homeMokebPooyesh'))

    else:
        return HttpResponse('چنددقیه دیگر مجدد تلاش کنید', content_type='text/plain')
       
