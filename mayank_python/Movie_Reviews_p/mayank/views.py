from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse("<h1>Rojesara Mayank </h1><br><h2>Roll no :137</h2>")
    #  return HttpResponse("<h1>137</h1>")
    