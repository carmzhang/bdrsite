from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import inspect
from django.db import connection
# Create your views here.

def index(request):
    return render(request,'members/index.html')
