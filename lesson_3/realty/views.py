from django.shortcuts import render

# Create your views here.
def realty_view(request):
    return render(request, 'realty/realty.html')