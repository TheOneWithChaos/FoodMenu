from django.shortcuts import render
from .models import Item
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    list= Item.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'detail.html', context)