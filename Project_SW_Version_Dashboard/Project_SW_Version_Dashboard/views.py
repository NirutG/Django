from django.http import HttpResponse, request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
import pyodbc # for MS SQL Server
from datetime import datetime # for DateTime
import random
import time


# def index(request):
#     return HttpResponse('Welcome to SAMAKARN StartUp101')

def about(request):
    return HttpResponse('This is testing Django Framework by NirutG')

def contact(request):
    return HttpResponse('Nirut Gammayeengoen, Tel : 089-113-9370')

def mainshop(request):
    return HttpResponse('Here is main shop for SAMAKARN.com')



def querydata_hsa(request):
    server = '10.4.32.55\INPXM20CRUS'
    database = 'DBXM20CRUS'
    username = 'wdm_spw'
    password = 'wdm_spw123'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    sql_query = """select top 17 * from VWD_XHSA_SUMMARY where TOOL_TYPE in ('1800')"""
    cursor.execute(sql_query)
    row = cursor.fetchone() 
    result = ''
    while row: 
        hsa_serial_number = row[0]
        tool_type = str(row[1])
        tool_start_date_time = str(row[2])
        row = cursor.fetchone()
        result = f" HSA_SERIAL_NUMBER = {hsa_serial_number}<br> TOOL_TYPE = {tool_type}<br> TOOL_START_DATE_TIME = {tool_start_date_time} "
    return HttpResponse(result)

def search(request, keyword, page):
    return HttpResponse(f'Search for : {keyword} page: {page}')

def date(request, day, month, year):
    return HttpResponse(f'Date: {day}-{month}-{year}')

def redirect(request, url):
    return HttpResponse(f'<a href="{url}" target="_blank"> \OPEN WEB</a>')

def show_article(request, id, title):
    return HttpResponse(f' ID: {id} <br>Title: {title}')

def drink(request, dnk):
    return HttpResponse(f'Drink: {dnk}')

def show_title(request, title):
    return HttpResponse(f'Title: {title}')

def find(request, key, page):
    page = int(page) # convert str to int
    prev = ''
    if page > 1:
        prev = f'<a href="/find/{key}/{page-1}">Previous</a>'
    else:
        prev = ''
    
    next = f'<a href="/find/{key}/{page+1}">Next</a>'
    
    return HttpResponse(f'{prev}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{next}')

def test_no_name(request, key1, key2):
    return HttpResponse(f'TEST NO Name: <br> Key1 : {key1}<br> Key2 : {key2}')

def maps(request):
    type = request.GET.get('type','hybrid')
    lat = request.GET.get('lat','13.7245601')
    lon = request.GET.get('lon', '100.4930241')
    zoom = request.GET.get('z', '11')

    return HttpResponse(f'Map Type : {type} <br> \
                          Location : {lat}, {lon} <br> \
                          Zoom : {zoom}')

def index(request):
    return render(request, 'index.html')

def sw_detail(request):
    return render(request, 'detail/detail.html')

def test_variables(request):
    dt = datetime.today()
    data = {
        'colors' : ['red', 'green', 'blue'],
        'flowers' : {'a':'rose', 'b':'jasmine', 'c':'orchid'},
        'date': dt
    }
    return render(request, 'test_variables.html', data)

def tag_if(request):
    vars = {'home_goals': 5, 'guest_goals': 5}
    return render(request, 'tag-if.html', vars)

def tag_for(request):
    vars = {
        'range': range(1, 6),
        'list': ['red', 'green', 'blue', 'yellow'],
        'dict': {'a':'ant', 'b':'boy', 'c':'cat', 'd':'dog'}
    }
    return render(request, 'tag-for.html', vars)

def filter_str_list_num(request):
    data = {
        'var_str': 'Hello World',
        'var_list': ['One', 'Two', 'Three'],
        'var_int': 2475,
        'var_float': 3.14,
        'var_none': None
    }
    return render(request, 'filter-str-list-num.html', data)

def filter_custom(request):
    now = datetime.today()
    return render(request, 'filter-custom.html', {'now':now})

def redirect_from(request):
    if random.randint(1, 10) < 5:
        return HttpResponseRedirect(reverse('redirect_to'))
    else:
        return redirect(redirect_error, code=123, text='Fetal Error')

def redirect_to(request):
    return render(request, 'redirect-to.html')

def redirect_error(request, code, text):
    return render(request, 'redirect-error.html', {'code':code, 'text':text})

def main(request):
    return render(request, 'main.html')

def main2(request):
    return render(request, 'main2.html')

def home(request):
    return render(request, 'home.html')

def products(request):
    data = {'products': ['Smartphone','Table','Notebook']}
    return render(request, 'products.html', data)

def static_media(request):
    return render(request, 'static-media.html')

def static_css(request):
    return render(request, 'static-css.html')

def static_js(request):
    return render(request, 'static-js.html')

def static_bootstrap(request):
    return render(request, 'static-bootstrap.html')

def dashboard_0950(request):
    check = 2
    bgcolor_index = 0
    bgcolor = ['#66FF33','#FFFF00','#FFFF00','#FF0000','#FF0000','#FF9900']
    css_class = ['table_cell_ti01','table_cell_ti02','border_right']
    sw_version_0950_exe = ['1.2.0.0','1.2.1.0']
    sw_version_0950_plc = ['2.13','2.12']
    sw_version_0950_hmi = ['2.08','2.07']
    sw_type = ['SW_EXE','SW_PLC','SW_HMI']

    state_dashboard_0950 = 1
    time_now = datetime.now()
    second_now = time_now.second
    state_dashboard_0950 = second_now
    # state_dashboard_0950 = 3


    dashboard_0950_data = {
    'fw' : ['FW33','FW34','FW35','FW36','FW37',':)'],
    'mc_line' : {'fpc':'FPC01',"other":'G1'},
    'sw_type' : sw_type[0],
    'sw_verson' : sw_version_0950_exe[0],
    'lines' : range(check),
    'css_class' : css_class[2],   
    'bgcolor' : bgcolor[bgcolor_index],
    'state_dashboard_0950' : state_dashboard_0950,  
    }   
    return render(request, 'sw_dashboards/dashboard_0950.html', dashboard_0950_data)


def temp(request):
    return render(request, 'temp.html')


# def test_something1():
#     current_datetime = datetime.now()

#     print('Test something')
#     print(current_datetime)
#     print(current_datetime.second)
#     print('Test something')
#     print('Test something5')

# test_something1()




