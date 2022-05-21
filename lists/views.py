from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
# from django.http import HttpResponse

from lists.models import Item, List
from lists.forms import ItemForm

def home_page(request):
    # if request.method == 'POST':
    #     new_item_text = request.POST.get('item_text', '')
    #     Item.objects.create(text=new_item_text)
    #     return redirect('/lists/the-only-list-in-the-world/')

    # items = Item.objects.all()
    return render(request, 'home.html', {'form': ItemForm()})#, {'items': items})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            text = request.POST.get('item_text', '')
            item = Item(text=text, list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"
    # items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    list_ = List.objects.create()
    text = request.POST.get('item_text', '')
    item = Item(text=text, list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)

# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     text = request.POST.get('item_text', '')
#     Item.objects.create(text=text, list=list_)
#     return redirect(f'/lists/{list_.id}/')