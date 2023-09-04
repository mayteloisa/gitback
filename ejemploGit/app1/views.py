from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def vista1(request):
    html="""
     <h1 style='color:blue'>
     Bienvenido!
     </h1> """
    return HttpResponse(html)

def vista2(request):
    dt=datetime.datetime.now()
    s="<b>Fecha y hora actual:</b>"+str(dt)
    return HttpResponse (s)
