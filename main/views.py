from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def IndexView(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def bomView(request):
    return render(request,'dash_bom.html')