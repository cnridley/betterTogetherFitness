from django.shortcuts import render

# Create your views here.

#view to return the guides page.

def guides(request):
 
    return render(request, 'products/guides.html')


#view to return the merch page

def merch(request):

    return render(request, 'products/merchandise.html')
