#from django.shortcuts import render
import zeep
import xmltodict
from django.shortcuts import render
from zeep import Client
from .forms import *
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
# Create your views here.

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
		form=getOilPriceForm()
	return render(request,'practica_soap/formulario_getOilPrice.html',{'form':form})



#CurrentOilPrice
def currentOilPrice(request):
	wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
	client = zeep.Client(wsdl=wsdl)
	result = client.service.CurrentOilPrice('EN')
	d = xmltodict.parse(result)
	print(result)
	print(d)
	oilPrices = set()

	return render(request, 'practica_soap/formulario_currentOilPrice.html', {'oilPrices': oilPrices})


