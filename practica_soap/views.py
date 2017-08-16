#from django.shortcuts import render
import zeep
import xmltodict
from django.shortcuts import render
from zeep import Client
from .forms import *
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
# Create your views here.

def mostrar_inidex(request):
    return render(request,'index.html')

def mostrar_formulario_getOilPrice(request):
    return render(request,'formulario_getOilPrice.html')

def mostrar_formulario_currentOilPrice(request):
    return render(request,'formulario_currentOilPrice.html')



def getOilPrice(request):
	if(request.method=="POST"):
		form=getOilPriceForm(request.POST)
		if(form.is_valid()):
			lenguaje=form.get_cleaned_data["lenguaje"]
			dia=form.get_cleaned_data["dia"]
			mes=form.get_cleaned_data["mes"]
			anio=form.get_cleaned_data["anio"]
			client = Client('http://www.pttplc.com/webservice/pttinfo.asmx?WSDL')
			results = client.service.GetOilPrice(lenguaje, dia, mes,anio)
			results = xmltodict.parse(results)
			results = results['PTT_DS']['DataAccess']
			return render(request,'practica_soap/results_getOilPrice.html',{'results':results})
		else:
			print('formulario no valido')
	else:
		form = getOilPriceForm()
	return render(request,'practica_soap/formulario_getOilPrice.html',{'form':form})

#CurrentOilPrice
def currentOilPrice(request):
	if(request.method=="POST"):
		form = currentOilPriceForm(request.POST)
		if(form.is_valid()):
			lenguaje = form.get_cleaned_data["lenguaje"]
			wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
			client = zeep.Client(wsdl=wsdl)
			result = client.service.CurrentOilPrice(lenguaje)
			return render(request, 'practica_soap/results_currentOilPrice.html', {'result': result})			
			#d = xmltodict.parse(result)
			#print(result)
			#print(d)
			#oilPrices = set()
		else:
			print('formulario no valido')
	else:
		form = currentOilPriceForm()
	return render(request, 'practica_soap/formulario_currentOilPrice.html', {'form' : form})