from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

def index(request):
    return render(request, 'index.html')


def charfield(request):
    if request.method == 'POST':
        form = CharFieldForm(request.POST)
    else:
        form = CharFieldForm()

    return render(request, 'charfield.html', {'form':form})

def number(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        q = request.POST.get('quantity', 0)
        p = request.POST.get('price', 0)
    else:
        form = NumberForm()
        q = 0
        p = 0

    try:
        total = int(q) * float(p)
    except:
        total = 0

    vars = {
        'form':form, 'quantity':q, 'price':p, 'total':total 
    }

    return render(request, 'number.html', vars)


def email_url(request):
    if request.method == 'POST':
        form = EmailURLForm(request.POST)
    else:
        form = EmailURLForm()
    
    return render(request, 'email-url.html', {'form': form})


def boolean(request):
    if request.method == 'POST':
        form = BooleanForm(request.POST)
    else:
        form = BooleanForm()
    
    return render(request, 'boolean.html', {'form': form})


def choice(request):
    if request.method == 'POST':
        #if form.is_valid():
            #checks = request.POST.getlist('font_style', [])
            #print(checks)
        
        form = ChoiceForm(request.POST)

    else:
        form = ChoiceForm()
    
    return render(request, 'choice.html', {'form': form})   


def date_time(request):
    if request.method == 'POST':
        form = DateAndTimeForm(request.POST)
    else:
        form = DateAndTimeForm()
    
    return render(request, 'date-time.html', {'form': form})


def crispy(request):
    if request.method == 'POST':
        form = CrispyForm(request.POST)
    else:
        form = CrispyForm()

    return render(request, 'crispy.html', {'form':form})