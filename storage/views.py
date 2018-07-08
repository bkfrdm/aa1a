from django.shortcuts import render, redirect

from .models import Supplier
# Create your views here.


def storage_search(request):
    if request.method == 'POST':
        Supplier.objects.create(di=request.POST['name_storage_search'])
        return redirect('/')

    suppliers = Supplier.objects.all()
    headers = {k: v for k, v in request.META.items() if k.startswith('HTTP_')}
    return render(request,
                  'storage/storage.html',
                  {'suppliers': suppliers,
                   'headers': headers.items()
                  })
