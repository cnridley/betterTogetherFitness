from django.shortcuts import render
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

    context = {
        'merch': merch,
    }

    return render(request, 'products/merchandise.html', context)
