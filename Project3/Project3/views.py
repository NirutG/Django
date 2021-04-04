from django.http import HttpResponse
import pyodbc # for MS SQL Server
import datetime # for DateTime


def index(request):
    return HttpResponse('Welcome to SAMAKARN StartUp101')

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

    #Sample select query
    # cursor.execute("SELECT @@version;") 
    # row = cursor.fetchone() 
    # while row: 
    #     print(row[0])
    #     row = cursor.fetchone()

    # print("##################### START : TESTING ##############################")
    sql_query = """select top 19 * from VWD_XHSA_SUMMARY where TOOL_TYPE in ('1800')"""
    cursor.execute(sql_query)
    row = cursor.fetchone() 
    result = ''
    while row: 
        hsa_serial_number = row[0]
        tool_type = str(row[1])
        tool_start_date_time = str(row[2])
        # print( hsa_serial_number + ' '+ tool_type )
        # print( hsa_serial_number + ' '+ tool_type + ' '+ tool_start_date_time )        
        row = cursor.fetchone()
        # print("##################### END : TESTING ##############################")
        # result = 'HSA_SERIAL_NUMBER : ' + hsa_serial_number + '--->' + 'TOOL_TYPE : '+ tool_type + '--->'  + 'TOOL_START_DATE_TIME : ' + tool_start_date_time
        # return HttpResponse(hsa_serial_number + ' '+ tool_type + ' '+ tool_start_date_time)
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