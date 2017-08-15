import xmltodict
import zeep

wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)
xml = client.service.GetOilPrice('EN', 10, 1, 2010)

res_dict = xmltodict.parse(xml)
print res_dict
print '\n\n'

lista = res_dict['PTT_DS']['DataAccess']

for i in range(len(lista)):
	for k,v in lista[i].items():
	   print(k, v)
