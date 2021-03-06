from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Merch, Category
from .forms import MerchForm


# Create your views here.
def all_merch(request):
    """ A view to show all merchandise """

    merch = Merch.objects.exclude(sku="UkraineDonation2022")
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'product_name':
                sortkey = 'lower_name'
                merch = merch.annotate(lower_name=Lower('product_name'))
            if sortkey == 'category':
                sortkey = 'category__product_name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            merch = merch.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            merch = merch.filter(category__product_name__in=categories)
            categories = Category.objects.filter(product_name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Nothing was entered")
                return redirect(reverse('merchandise'))

            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            merch = merch.filter(queries)

    current_sorting = f'{sort}-{direction}'

    context = {
        'merch': merch,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'merchandise/merchandise.html', context)


def merchandise_info(request, merch_id):
    """ A view to show the merchandise's details """

    merch = get_object_or_404(Merch, id=merch_id)

    context = {
        'merch': merch,
    }

    return render(request, 'merchandise/merchandise_info.html', context)


@login_required
def add_merchandise(request):
    """ Adds merchandise to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorised users can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MerchForm(request.POST, request.FILES)
        if form.is_valid():
            merch = form.save()
            messages.success(request, 'Successfully added merchandise!')
            return redirect(reverse('merchandise_info', args=[merch.id]))
        else:
            messages.error(request, 'Failed to add merchandise. Please ensure the form is valid.')
    else:
        form = MerchForm()

    template = 'merchandise/add_merchandise.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_merchandise(request, merch_id):
    """ Edits merchandise in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorised users can do that.')
        return redirect(reverse('home'))

    merch = get_object_or_404(Merch, id=merch_id)
    if request.method == 'POST':
        form = MerchForm(request.POST, request.FILES, instance=merch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated merchandise!')
            return redirect(reverse('merchandise_info', args=[merch.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = MerchForm(instance=merch)
        messages.info(request, f'You are editing {merch.product_name}')

    template = 'merchandise/edit_merchandise.html'
    context = {
        'form': form,
        'product': merch,
    }

    return render(request, template, context)


@login_required
def delete_merchandise(request, merch_id):
    """ Deletes selected merchandise from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorised users can do that.')
        return redirect(reverse('home'))
    merch = get_object_or_404(Merch, id=merch_id)
    merch.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('merchandise'))
