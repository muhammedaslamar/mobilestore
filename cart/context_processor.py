from .models import *
from .views import *
def count(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=cart_list.objects.filter(cart_id=cartid(request))
            cti=item.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count+=c.quan
        except:
            cart_list.DoesNotExist
            item_count=0
    return dict(itc=item_count)