from django.shortcuts import render, get_object_or_404
from .models import Merch

# Create your views here.
def all_merch(request):
    """ A view to show all merchandise """

    merch = Merch.objects.all()

    context = {
        'merch': merch,
    }

    return render(request, 'merchandise/merchandise.html', context)


def merchandise_info(request, merch_id):
    """ A view to show the merchandise's details """

    merch = get_object_or_404(Merch, id=merch_id)

    context = {
        'merch': merch,
    }

    return render(request, 'merchandise/merchandise_info.html', context)