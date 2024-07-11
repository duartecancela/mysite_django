from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse('This is an item view')

def detail(request,item_id):
    return HttpResponse('This is an item id: %s' % item_id)