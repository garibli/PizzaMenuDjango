from django.shortcuts import render, redirect
from Ornek.models import Item
from Ornek.forms import ItemForm

def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after adding the item
    else:
        form = ItemForm()
    return render(request, 'index.html', {'form': form, 'items': Item.objects.all()})

def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm(instance=item)
    return render(request, 'update_item.html', {'form': form})

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'delete_item.html', {'item': item})
