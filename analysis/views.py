# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import inspect
from .forms import CustomQueryForm, QueryDropdownForm, FillQueryForm, MapForm
from .models import QueryDropdown
from django.db import connection
import array
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib import pylab
#from pylab import *


query_dict = {'1':'SELECT site_id, cfu, ctx FROM plate JOIN agar ON plate.agar_id = agar.agar_id', '2':'two'}

def index(request): # GET
	# create blank forms
	template_name = 'analysis/index.html'
	fill_sql_form = FillQueryForm()
	custom_sql_form = CustomQueryForm()
	dropdown_form = QueryDropdownForm()
	map_form = MapForm()
	return render(request, template_name, {'custom_sql_form': custom_sql_form, 'dropdown_form': dropdown_form, 'fill_sql_form':fill_sql_form, 'map_form':map_form})

# CUSTOM SQL
def get_custom_query(request): # POST
	# create a form instance and populate it with data from the request
	sql_form = CustomQueryForm(request.POST)
	# check if it's valid
	if sql_form.is_valid():
		# process the data in form.cleaned_data as required
		query = sql_form.cleaned_data['query']

		try:
			result = execute_query(query)
			colnames = result[0].keys
			num_rows = len(result)
			return render(request, 'analysis/query.html', {'query':query, 'num_rows':num_rows, 'result':result, 'colnames':colnames})
		except:
			return HttpResponse("There were one or more errors in your query. Please try again.")
	else:
		return HttpResponse("Could not execute query.")

# DROPDOWN
def get_selection(request):
	dropdown_form = QueryDropdownForm(request.POST)
	if dropdown_form.is_valid():
		query_num = dropdown_form.cleaned_data['query']
		query = query_dict[query_num]
		result = execute_query(query)
		colnames = result[0].keys
		num_rows = len(result)
		# return BarView.as_view()
		#graphic = plot(result,colnames)
#		return render(request, 'analysis/query.html', {'query':query, 'num_rows':num_rows, 'result':result, 'colnames':colnames, 'graphic':graphic, 'preselected':True})
	else:
		return HttpResponse("Could not execute selection.")

#def plot(countArray,NameArray):
   # x = django_numpy.linspace(1,len(NameArray),len(NameArray))
#    x = linspace(1,len(NameArray),len(NameArray))
#    fig = plt.figure()
#    plt.bar(x, countArray)
#    plt.xlabel('Sites')
#    plt.ylabel('Average CFU Count')
#    plt.xticks(x, NameArray, ha = 'left', rotation=315, wrap='True')
#    plt.xticks(size = 6)

#    canvas = fig.canvas
#    buf, size = canvas.print_to_buffer()
#    image = Image.frombuffer('RGBA', size, buf, 'raw', 'RGBA', 0, 1)
#    buffer=io.BytesIO()
#    image.save(buffer,'PNG')
#    graphic = buffer.getvalue()
#    graphic = base64.b64encode(graphic)
#    buffer.close()
#    return graphic

# FILL IN SQL
def get_query(request):
	sql_form = FillQueryForm(request.POST)
	if sql_form.is_valid():
# process the data in form.cleaned_data as required
		select = sql_form.cleaned_data['select']
		from_field = sql_form.cleaned_data['from_field']
		where = sql_form.cleaned_data['where']
		limit = sql_form.cleaned_data['limit']
		query = 'SELECT ' + select + ' FROM ' + from_field + ' WHERE ' + where + ' LIMIT ' + limit
		try:
			result = execute_query(query)
			colnames = result[0].keys
			num_rows = len(result)
			return render(request, 'analysis/query.html', {'query':query, 'num_rows':num_rows, 'result':result, 'colnames':colnames})
    		except:
			return HttpResponse("There were one or more errors???!!!!!!!!! in your query. Please try again.")
        else:
		return HttpResponse("Could not execute query.")

#test_query

#def test_query(request):
#    a = request.arg,get('que',type =str)
#    sql_form=FillQueryForm(request.POST)
#    return HttpResponse("23333333")

# GOOGLE MAP
def get_map(request):
	return render(request, 'analysis/map.html')

def execute_query(query):
	with connection.cursor() as cursor:
		cursor.execute(query)
		return dictfetchall(cursor)
	# ex: [{'parent_id': None, 'id': 54360982}, {'parent_id': None, 'id': 54360880}]

def dictfetchall(cursor):
	# Return all rows from a cursor as a dict
	columns = [col[0] for col in cursor.description]
	return [
    	dict(zip(columns, row))
    	for row in cursor.fetchall()
    ]
