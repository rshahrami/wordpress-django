from django.shortcuts import render
from post.models import *
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def HomePageViews(request):
    return render(request, 'postTemplate.html')
