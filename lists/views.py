from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    # if request.method == 'POST':
    context = {
        'new_item_text': request.POST.get('item_text', ''),
    }
        # return render(request, 'home.html', context)

    return render(request, 'home.html', context)