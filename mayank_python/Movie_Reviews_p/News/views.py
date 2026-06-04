from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import News
def News1(request):
    newss=News.objects.all().order_by('-date')
    return render(request,'news.html',{'newss':newss})