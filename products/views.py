from django.shortcuts import render
from products.models import Gallery
from products.models import nutritionGuides

# Create your views here.

#view to return the guides page.


def guides(request):

    gallery = Gallery.objects.all() #gets the images from th egallery model 
    guides = nutritionGuides.objects.all() #gets all the info from the nutrition guides.

    context = {
        'gallery': gallery,
        'guides': guides,
    }
 
    return render(request, 'products/guides.html', context)


#view to return the merch page

def merch(request):

    return render(request, 'products/merchandise.html')
