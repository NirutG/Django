from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def product_detail(request):
    return render(request, 'products/detail.html')


def variable(request):
    #data = {'name': 'T-Shirt', 'price': 500, 'descr': 'Very Good Shirt'}
    from datetime import date
    d = date.today()
    data = {
        'colors': ['red', 'green', 'blue'],
        'flowers': {'a':'rose', 'b':'jasmine', 'c':'orchid'},
        'is_valid': True,
        'dt': d
    }
    return render(request, 'variable.html', data)


def tag_if(request):
    vars = {
        'home_goals': 3, 
        'guest_goals': 2,
    }
    return render(request, 'tag-if.html', vars)


def tag_for(request):
    vars = {
        'range': range(1, 6),
        'list': ['red', 'green', 'blue', 'yellow'],
        'dict': {'a':'ant', 'b':'boy', 'c':'cat', 'd':'dog'}
    }
    return render(request, 'tag-for.html', vars)


def tag_auto_escape(request):
    data = {
        'html_str': '<b>\'Tom\' & "Jerry"</b>',
    }
    return render(request, 'tag-auto-escape.html', data)


def tag_others(request):
    return render(request, 'tag-others.html', {'list':[1, 3, 5, 7]})


def filter_str_list_num(request):
    data = {
        'var_str': 'Hello World',
        'var_list': ['One', 'Two', 'Three'],
        'var_int': 2475,
        'var_float': 3.14,
        'var_none': None
    }
    return render(request, 'filter-str-list-num.html', data)    

def filter_num(request):
    data = {
        'hahaha':555,
        'filesize':387504257,
        'num_int':1234,
        'num_float':1234.56789
    }
    return render(request, 'filter-num.html', data)   


def filter_string(request):
    data = {
		'str1': 'Model Template View',
		'str2': 'model<br>\nview<br>\ncontroller',
		'str3': 'django is the web framework',
		'str4': "<b>Don't repeat youself (DRY)</b>",
        'str5': '<b><a href=#>Click Here</a> to download</b>'
    }
    return render(request, 'filter-string.html', data)


def filter_special_chars(request):
	data = {
		'str1': 'I\'m using "Django"',
		'str2': 'line1\nline2\nline3',
	}
	return render(request, 'filter-special-chars.html', data)


def filter_url(request):
	data = {
		'str1': 'Please visit: www.example.com or https://go.to/xyz',
		'str2': 'Send you data to admin@example.com',
		'str3': 'Download at https://example.com/?file=django.zip'
	}
	return render(request, 'filter-url.html', data)


def filter_datetime(request):
    from datetime import datetime, date
    from datetime import timedelta

    now = datetime.today()
    next_45_days = now + timedelta(days=45)
    year = now.year
    data = {
        'now': now,
        'next45days': next_45_days,
        'newyear': date(year, 1, 1),
        'valentine': date(year, 2, 14),
        'oldyear':date(year, 12, 31)
    }
    return render(request, 'filter-datetime.html', data)


def filter_custom(request):
    from datetime import datetime

    now = datetime.today()
    return render(request, 'filter-custom.html', {'a':10, 'now':now})


def redirect_from(request):
    import random
    
    if random.randint(1, 10) < 5:
        #return redirect('/redirect/to')            #ระบุตำแหน่งพาธโโยตรง (ไม่ยืดหยุ่น)
        #return redirect(redirect_to)               #ระบุชื่อฟังก์ชันวิว
        return redirect('redirect_to')             #ระบุเป็นชื่อพาธ
        #return redirect(reverse('redirect_to'))     #ระบุโดยนำชื่อพาธมาแปลงด้วยฟังก์ชัน reverse()
    else:
        return redirect(redirect_error, code=123, text='Fetal Error')
        #return redirect('redirect_error', code=123, text='Unknown Error')
        #return redirect(reverse('redirect_error', kwargs={'code':123, 'text':'Unknown Error'}))
        
        
def redirect_to(request):
    return render(request, 'redirect-to.html')


def redirect_error(request, code, text):
    return render(request, 'redirect-error.html', {'code':code, 'text':text})


def main(request):
    return render(request, 'main.html')


def home(request):
    return render(request, 'home.html')


def products(request):
    data = {
        'products':['Smartphone', 'Tablet', 'Notebook']
    }
    return render(request, 'products.html', data)