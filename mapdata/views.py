
from django.shortcuts import render

def index(request):
	return render(request, 'mapdata/index.html', context)