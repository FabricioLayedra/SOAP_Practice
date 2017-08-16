#from django.shortcuts import render
import zeep
import xmltodict
from django.shortcuts import render
from zeep import Client
from .forms import *
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
# Create your views here.

def mostrar_index(request):
    return render(request,'soap/index.html')

def mostrar_formulario_getOilPrice(request):
    return render(request,'soap/formulario_getOilPrice.html')

def mostrar_formulario_currentOilPrice(request):
    return render(request,'soap/formulario_currentOilPrice.html')



def getOilPrice(request):
	if(request.method=="POST"):
		form=getOilPriceForm(request.POST)
		if(form.is_valid()):
			lenguaje=form.cleaned_data["lenguaje"]
			dia=form.cleaned_data["dia"]
			mes=form.cleaned_data["mes"]
			anio=form.cleaned_data["anio"]
			client = Client('http://www.pttplc.com/webservice/pttinfo.asmx?WSDL')
			results = client.service.GetOilPrice(lenguaje, dia, mes,anio)
			results = xmltodict.parse(results)
			results = results['PTT_DS']['DataAccess']
			return render(request,'soap/results_getOilPrice.html',{'results':results})
		else:
			print('formulario no valido')
	else:
		form = getOilPriceForm()
	return render(request,'soap/formulario_getOilPrice.html',{'form':form})

#CurrentOilPrice
def currentOilPrice(request):
	if(request.method=="POST"):
		form = currentOilPriceForm(request.POST)
		if(form.is_valid()):
			lenguaje = form.cleaned_data["lenguaje"]
			wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
			client = Client('http://www.pttplc.com/webservice/pttinfo.asmx?WSDL')
			result = client.service.CurrentOilPrice(lenguaje)			
			results = xmltodict.parse(result)
			results = results['PTT_DS']['DataAccess']
			return render(request, 'soap/results_currentOilPrice.html', {'results': results})
			#print(result)
			#print(d)
			#oilPrices = set()
		else:
			print('formulario no valido')
	else:
		form = currentOilPriceForm()
	return render(request, 'soap/formulario_currentOilPrice.html', {'form' : form})