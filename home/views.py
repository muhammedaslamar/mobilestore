from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
def home(request,c_slug=None):
        c_page = None
        prdt = None
        if c_slug != None:
            c_page = get_object_or_404(categ, slug=c_slug)
            prdt = product.objects.filter(category=c_page, available=True)
        else:
            prdt = product.objects.all().filter(available=True)
        cart = categ.objects.all()

        paginator = Paginator(prdt, 12)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            pro = paginator.page(page)
        except(EmptyPage, InvalidPage):
            pro = paginator.page(paginator.num_pages)

        return render(request,'index.html',{'pr':prdt,'ct':cart,'pg':pro})
def prodetails(request,c_slug,p_slug):
    try:
        prdt=product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'pr':prdt})



def search(request):
    prdt=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prdt=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prdt})