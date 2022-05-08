from django.shortcuts import render, redirect
# from django.http import HttpResponse

from lists.models import Item

def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')

    # new_item_text = ''

    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
        Item.objects.create(text=new_item_text)
        return redirect('/')
        # item.text = new_item_text
        # item.save()

    # context = {
    #     'new_item_text': new_item_text,
    # }
        # return render(request, 'home.html', context)
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items}) #, context)