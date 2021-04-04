from django.shortcuts import render
from django.http import JsonResponse
from .forms import LoginForm
import random
import time


def index(request):
    return render(request, 'index.html')


def ajax_random(request):
    if request.is_ajax():
        r = random.randint(100, 1000)
        return JsonResponse({'num':r})
    else:
        return render(request, 'ajax-random.html')


def ajax_login(request):
    if request.is_ajax():
        if 'login' in request.GET:
            login = request.GET['login']
            
            login_exist = False
            if login.lower() in ['admin', 'python', 'django']:
                login_exist = True
        else:
            login_exist = None

        return JsonResponse({'exist':login_exist})

    else:
        form = LoginForm()
        return render(request, 'ajax-login.html', {'form':form})


def ajax_cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
        request.session.set_expiry(0)

    cart = request.session['cart']

    #ถ้ามีข้อมูลส่งขึ้นมาในแบบ AJAX 
    #หากไม่ซ้ำกับรายการที่มีอยู่แล้ว ก็ให้เพิ่มเข้าไป
    if request.is_ajax():
        if request.method == 'POST':
            p = request.POST.get('product', None)
  
            if p not in cart:
                cart += [p]

            request.session['cart'] = cart
        
        return JsonResponse({'cart':cart})

    else:
        #ถ้าไม่ใช่การส่งข้อมูลเข้ามา ให้สร้างรายการสินค้า
        #เป็นคำว่า "Product X" แล้วส่งกลับไปแสดงผลที่เท็มเพลต
        products = [f'Product {x}' for x in range(1, 11)]
        return render(request, 'ajax-cart.html', {'products':products,'cart':cart})


def ajax_clear_cart(request):
    request.session['cart'] = []
    return JsonResponse({})


def ajax_overlay(request):
    if request.is_ajax():
        time.sleep(2)   #หน่วงเวลา 2 วินาที
        return JsonResponse({})
    else:
        return render(request, 'ajax-overlay.html')