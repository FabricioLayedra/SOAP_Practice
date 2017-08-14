#from django.shortcuts import render
import zeep
import xmltodict
# Create your views here.






#CurrentOilPrice
def listarOilPrices(request):
    
	wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
	client = zeep.Client(wsdl=wsdl)
	result = client.service.CurrentOilPrice('EN')
	d = xmltodict.parse(result)
	print(result)
	print(d)
	oilPrices = set()

	return render(request, 'practica_soap/listar_current.html', {'oilPrices': oilPrices})