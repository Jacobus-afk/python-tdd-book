from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
# from django.http import HttpResponse

from lists.models import Item, List
from lists.forms import ItemForm

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            # text = request.POST.get('text', '')
            # Item.objects.create(text=text, list=list_)
            form.save(for_list=list_)
            return redirect(list_)
        # try:
        #     text = request.POST.get('text', '')
        #     item = Item(text=text, list=list_)
        #     item.full_clean()
        #     item.save()
        #     return redirect(list_)
        # except ValidationError:
        #     error = "You can't have an empty list item"
    # items = Item.objects.filter(list=list_)

    # form = ItemForm()
    context = {'list': list_, 'form': form}

    return render(request, 'list.html', context)


def new_list(request):
    # list_ = List.objects.create()
    # text = request.POST.get('text', '')
    # item = Item(text=text, list=list_)
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        # text = request.POST.get('text', '')
        # Item.objects.create(text=text, list=list_)
        form.save(for_list=list_)
        return redirect(list_)
    return render(request, 'home.html', {"form": form})
    # try:
    #     item.full_clean()
    #     item.save()
    # except ValidationError:
    #     list_.delete()
    #     error = "You can't have an empty list item"
    #     return render(request, 'home.html', {"error": error})
    # return redirect(list_)
