from django.shortcuts import render
from .forms import CustomForm

# Create your views here.

def list(request):
    return render(request, 'extendtest/list_goods.html')



def login(request):
    if request.method=='GET':
        form = CustomForm()
        return render(request, 'extendtest/login.html',{'form':form})






