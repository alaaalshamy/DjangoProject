from django.shortcuts import render
from .models import Writer
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    num_authors=Writer.objects.count()
    
    
    return render(
        request,
        'liberary/index.html',
        {'num_authors':num_authors},
    )

def Writer_view(request,pk):
    model = Writer

    Writer_list=Writer.objects.get(pk=pk)
    context = {
        "temp" : Writer_list
    }
    
    return render(
        request,
        'liberary/base_generic.html',
        context
    )





