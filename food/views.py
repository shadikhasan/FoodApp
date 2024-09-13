from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required


# Create your views here.
def food(request):
    item_list = Item.objects.all()
    return render(request, "items.html",{
        'item_list': item_list,
    })

def details(request, item_id):
    detail = Item.objects.get(pk=item_id)
    return render(request, "item.html", {
        'item': detail,
    })

@login_required
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food')
    
    return render(request, 'item-form.html', {
        'form': form
    })

@login_required
def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food')

    return render(request, 'item-form.html', {
        'form': form,
        'item': item,
    })
@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food')  # Adjust this to the correct redirect view

    return render(request, 'delete-item.html', {'item': item})


def index(request):
    return redirect('/food/')