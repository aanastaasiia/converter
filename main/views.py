from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    context = requests.get('https://v6.exchangerate-api.com/v6/b04be2ccc08afe25554f301e/latest/USD').json()
    if request.method == 'GET':
        return render(request=request, template_name='index.html', context=context)

def sendform(request):
    context = requests.get('https://v6.exchangerate-api.com/v6/b04be2ccc08afe25554f301e/latest/USD').json()
    amount = str(request.POST.get("amount"))
    value1 = str(request.POST.get("value1"))
    value2 = str(request.POST.get("value2"))
    amount = round(int(amount)/(int(context['conversion_rates'][str(value1)]))*(int(context['conversion_rates'][str(value2)])), 2)
    context['amount'] = amount
    context['value'] = value2

    return render(request=request, template_name='result.html', context=context)
    
    

     
     