from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from home.models import *
from django.core.exceptions import ObjectDoesNotExist
def cart(request,tot=0,count=0,ct_items=None):
        try:
                ct = cart_list.objects.get(cart_id=cartid(request))
                ct_items = item.objects.filter(cart=ct, active=True)
                for i in ct_items:
                        tot += (i.prodt.price * i.quan)
                        count += i.quan
        except ObjectDoesNotExist:
                pass
        return render(request,'checkout.html',{'ci':ct_items,'t':tot,'c':count})

def cartid(request):
        ct_id=request.session.session_key
        if not ct_id:
                ct_id=request.session.create()
        return ct_id

def add_cart(request,product_id):
        prd=product.objects.get(id=product_id)
        try:
                ct=cart_list.objects.get(cart_id=cartid(request))
        except cart_list.DoesNotExist:
                ct=cart_list.objects.create(cart_id=cartid(request))
                ct.save()
        try:
                c_items=item.objects.get(prodt=prd,cart=ct)
                if c_items.quan < c_items.prodt.stock:
                        c_items.quan+=1
                c_items.save()
        except item.DoesNotExist:
                c_items=item.objects.create(prodt=prd,cart=ct,quan=1)
                c_items.save()
        return redirect('cart')

def mincart(request,product_id):
        ct=cart_list.objects.get(cart_id=cartid(request))
        prod=get_object_or_404(product,id=product_id)
        c_items=item.objects.get(prodt=prod,cart=ct)
        if c_items.quan>1:
                c_items.quan-=1
                c_items.save()
        else:
                c_items.delete()
        return redirect('cart')
def delete(request,product_id):
        ct = cart_list.objects.get(cart_id=cartid(request))
        prod = get_object_or_404(product, id=product_id)
        c_items = item.objects.get(prodt=prod,cart=ct)
        c_items.delete()
        return redirect('cart')



