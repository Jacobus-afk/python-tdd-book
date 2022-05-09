from django.shortcuts import render, redirect
# from django.http import HttpResponse

from lists.models import Item, List

def home_page(request):
    # if request.method == 'POST':
    #     new_item_text = request.POST.get('item_text', '')
    #     Item.objects.create(text=new_item_text)
    #     return redirect('/lists/the-only-list-in-the-world/')

    # items = Item.objects.all()
    return render(request, 'home.html')#, {'items': items})

def view_list(request, list_id):
    # items = Item.objects.all()
    list_ = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    text = request.POST.get('item_text', '')
    Item.objects.create(text=text, list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    text = request.POST.get('item_text', '')
    Item.objects.create(text=text, list=list_)
    return redirect(f'/lists/{list_.id}/')