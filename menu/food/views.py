from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse
from django.template import loader
from .forms import ItemForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# def index(request):
#     list= Item.objects.all()
#     context = {
#         'list': list,
#     }
#     return render(request, 'index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'list'
    paginate_by = 2
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        else:
            return Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'detail.html', context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'detail.html'
    

# def add_item(request):
#     form = ItemForm(request.POST or None) 
    
#     if form.is_valid():
#         form.save()
#         form = ItemForm() # Clear the form after saving
#         return redirect('food:index')
    
#     return render(request, 'item_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CreateItem(CreateView):
    model = Item
    fields = ['name', 'description', 'price', 'image']
    template_name = 'item_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'item_form.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'delete_item.html', {'item': item})
    
def logout_user(request):
    logout(request)
    return render(request, 'logout.html')