from django.shortcuts import render
from mokeb.models import *
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect
from django_ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='50/m')
def PostViewsMokebPooyesh(request):

    posts = PooyeshMokebModel.objects.all().order_by('?')

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 30)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'files': users}

    return render(request, 'MokebTemplate.html', context)

@ratelimit(key='ip', rate='50/m')
def MaxPostLikeMokebPooyesh(request):

    posts = PooyeshMokebModel.objects.all().order_by('-like')

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 30)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'files': users}

    return render(request, 'MokebTemplate.html', context)

@ratelimit(key='ip', rate='50/m')
def LastDateMokebPooyesh(request):
    posts = PooyeshMokebModel.objects.all().order_by('-id')

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 30)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'files': users}

    return render(request, 'MokebTemplate.html', context)


def CaptchaViewMokebPooyesh(request):

    return render(request, 'captcha.html')

@ratelimit(key='ip', rate='50/m')
def SearchByIdMokebPooyesh(request , id):
    try:
        id = int(id)
        posts = PooyeshMokebModel.objects.filter(id=id)
        context = {'posts': posts}
        return render(request, 'retrymokeb.html' , context)
    except:
        return redirect(reverse('homeMokebPooyesh'))


@csrf_exempt
@ratelimit(key='ip', rate='50/m')
def UpdateLikeMokebPooyesh(request):
    # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        print(request.POST)

        print(request.POST['id'])
        post = PooyeshMokebModel.objects.get(id=request.POST['id'])
        print(post.like)
        post.like = post.like+1
        post.save()
        # save the data and after fetch the object in instance

        # send to client side.
        return JsonResponse({"instance": 'hellow owrld'}, status=200)