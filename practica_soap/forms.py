from django import forms

class currentOilPriceForm(forms.Form):
	lenguaje = forms.CharField(max_length=10)


class getOilPriceForm(forms.Form):
	lenguaje = forms.CharField(max_length=10)
	dia = forms.IntegerField()
	mes = forms.IntegerField()
	anio = forms.IntegerField()