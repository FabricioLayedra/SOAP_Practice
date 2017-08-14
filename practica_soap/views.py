<<<<<<< HEAD
#from django.shortcuts import render
import zeep
import xmltodict
=======
from django.shortcuts import render
from zeep import Client
from .forms import *
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
>>>>>>> 15705cd7e06ad8f9ec576d75e4f33d7ef6aeb219
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
			result = client.service.GetOilPrice(lenguaje, dia, mes,anio)
			return render(request,'practica_soap/results_getOilPrice.html',{'results':results})

		else:
			print('formulario no valido')
	else:
		form=getOilPriceForm()
	return render(request,'practica_soap/formulario_getOilPrice.html',{'form':form})






#CurrentOilPrice
<<<<<<< HEAD
def listarOilPrices(request):
    
	wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
	client = zeep.Client(wsdl=wsdl)
	result = client.service.CurrentOilPrice('EN')
	d = xmltodict.parse(result)
	print(result)
	print(d)
	oilPrices = set()

	return render(request, 'practica_soap/listar_current.html', {'oilPrices': oilPrices})
=======
wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)
result = client.service.CurrentOilPrice('EN')
>>>>>>> 15705cd7e06ad8f9ec576d75e4f33d7ef6aeb219
