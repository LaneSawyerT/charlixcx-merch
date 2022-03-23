from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Merch

# Create your views here.
def all_merch(request):
    """ A view to show all merchandise """

    merch = Merch.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Nothing was entered")
                return redirect(reverse('merchandise'))
            
            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            merch = merch.filter(queries)

    context = {
        'merch': merch,
        'search_term': query,
    }

    return render(request, 'merchandise/merchandise.html', context)


def merchandise_info(request, merch_id):
    """ A view to show the merchandise's details """

    merch = get_object_or_404(Merch, id=merch_id)

    context = {
        'merch': merch,
    }

    return render(request, 'merchandise/merchandise_info.html', context)