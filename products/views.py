from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from products.models import Gallery
from products.models import nutritionGuides
from products.models import merchandise

# Create your views here.


def guides(request):

    gallery = Gallery.objects.all()  # gets the images from the gallery model 
    guides = nutritionGuides.objects.all()  # gets all the info from the nutrition guides.

    context = {
        'gallery': gallery,
        'guides': guides,
    }
 
    return render(request, 'products/guides.html', context)


#view to return the merch page

def merch(request):

    merch = merchandise.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            merch = merch.filter(queries)

    context = {
        'merch': merch,
        'search_term': query,
    }

    return render(request, 'products/merchandise.html', context)


def merch_detail(request, merch1_id):
    """ A view to show individual product details """

    merch1 = get_object_or_404(merchandise, pk=merch1_id)

    context = {
        'merch1': merch1,
    }

    return render(request, 'products/merch_details.html', context)