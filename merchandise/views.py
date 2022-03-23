from django.shortcuts import render
from .models import Merch

# Create your views here.
def all_merch(request):
    """ A view to show all merchandise """

    merch = Merch.objects.all()

    context = {
        'merch': merch,
    }

    return render(request, 'merchandise/merchandise.html', context)