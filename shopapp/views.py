from django.shortcuts import render, get_object_or_404
from shopapp.models import products, categ
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prod=products.objects.filter(category=c_page,available=True)
    else:
        prod=products.objects.all().filter(available=True)
    cat=categ.objects.all()
    return render(request, "index.html",{'pr':prod,'ct':cat})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod = products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})