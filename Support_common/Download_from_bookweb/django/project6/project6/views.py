from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm, ProductForm

def index(request):
    return render(request, 'index.html')


def request_obj(request):
    vars = {
        'path': request.path,
        'full_path': request.get_full_path(),
        'host': request.get_host(),
        'method': request.method,
        'is_secure': request.is_secure()
    }
    return render(request, 'request-obj.html', vars)


def form_get(request):
	q = request.GET.get('q', None)
	return render(request, 'form-get.html', {'q': q})


def form_post(request):
    #ถ้าไม่มีข้อมูลส่งจากฟอร์มเข้ามา ให้แสดงเพจที่บรรจุฟอร์ม
    #แต่ถ้ามีข้อมูลส่งเข้ามา ให้ส่งข้อมูลไปยังเพจการแสดงผล
    if 'firstname' not in request.POST:
        return render(request, 'form-post.html')  
    else:
        #อ่านข้อมูลที่ถูกส่งเข้ามาแล้วเก็บในตัวแปร เพื่อส่งไปยังเพจเป้าหมาย
        vars = {
            'fname': request.POST.get('firstname', None),
            'lname': request.POST.get('lastname', None)
        }
        return render(request, 'form-post.html', vars)


def search(request):
    form = SearchForm(request.GET)

    vars = {
        'form': form,
        #'kw': kw #request.GET.get('search', '')
    }
    return render(request, 'search.html', vars)

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()

    vars = {
        'form': form
    }
    return render(request, 'product.html', vars)

def field_args(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()

    return render(request, 'field-args.html', {'form':form}) 

def as_table(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()

    return render(request, 'form-as-table.html', {'form':form}) 

def as_p(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()

    return render(request, 'form-as-p.html', {'form':form})

def crispy(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()

    return render(request, 'form-crispy.html', {'form':form})

