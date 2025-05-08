from django.shortcuts import render

from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    ice_cream = IceCream.objects.get(id=pk)
    context = {
        'ice_cream': ice_cream
    }
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_cream_list = IceCream.objects.all()
    context = {
        'ice_cream_list': ice_cream_list
    }
    return render(request, template, context)
