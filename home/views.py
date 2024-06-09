from django.shortcuts import render
from account.models import Footer


# Create your views here.
def home_view(request):
    footer = Footer.objects.last()
    return render(request, 'home/home.html', context={"footer": footer})
