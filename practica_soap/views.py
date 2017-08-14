from django.shortcuts import render

# Create your views here.






#CurrentOilPrice
wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)
result = client.service.CurrentOilPrice('EN')