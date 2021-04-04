from django.shortcuts import render
from database.models import Employee, EmployeeForm, Member, MemberForm
from .forms import SearchForm
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def employee_create(request):
    #ถ้ามีข้อมูลจากฟอร์มถูกส่งเข้ามาด้วยเมธอด POST
    if request.method == 'POST':
        #สร้างอินสแตนซ์ของโมเดลฟอร์ม
        form = EmployeeForm(request.POST)

        #ถ้าข้อมูลทั้งหมดถูกต้อง
        if form.is_valid():
            #บันทึกข้อมูลลงในฟิลด์ต่างๆ
            form.save()

    else:
        form = EmployeeForm()
    
    return render(request, 'employee-create.html', {'form': form})

def employee_read(request):
    data = Employee.objects.all()
    return render(request, 'employee-read.html', {'data': data})

def employee_search(request):
    if request.method=='POST':
        kw = request.POST.get('name', '')
        form = SearchForm(request.POST, initial={'name': kw})
    else:
        kw = request.GET.get('name', '')
        form = SearchForm(initial={'name': kw})
    
    data = Employee.objects.filter(
                Q(firstname__contains=kw) | 
                Q(lastname__contains=kw))[:10]
    
    return render(request, 'employee-search.html', {'form': form, 'data': data})

def employee_edit(request):
    data = Employee.objects.all()
    return render(request, 'employee-edit.html', {'data': data})

def employee_update(request, id):
    #ถ้ามีข้อมูลจากฟอร์มถูกส่งเข้ามาด้วยเมธอด POST
    if request.method == 'POST':
        #อ่านข้อมูลเดิม
        row = Employee.objects.get(id=id) #get_object_or_404(Employee, id=id)

        #กำหนดข้อมูลเดิมให้กับโมเดลฟอร์ม เพื่อเปรียบเทียบกับข้อมูลใหม่ที่รับเข้ามา
        form = EmployeeForm(instance=row, data=request.POST)

        #ถ้าข้อมูลทั้งหมดถูกต้อง
        if form.is_valid():
            #บันทึกการเปลี่ยนแปลงลงในฟิลด์ต่างๆ
            form.save()
    else:
        #ถ้าไม่มีข้อมูลส่งจากโมเดลฟอร์มเข้ามา 
        #ให้อ่านข้อมูลเดิม เพื่อนำไปกำหนดเป็นค่าเริ่มแรกของอินพุทแต่ละอัน

        #วิธีที่ 1
        row = Employee.objects.get(id=id)
        form = EmployeeForm(initial=row.__dict__)

        #วิธีที่ 2
        #rows = Employee.objects.filter(id=id).values()
        #form = EmployeeForm(initial=rows[0])

    return render(request, 'employee-update.html', {'form': form})


def employee_delete(request, id):
    Employee.objects.get(id=id).delete()

    data = Employee.objects.filter()[:10]
    return render(request, 'employee-edit.html', {'data': data})


def member_signin(request):
    if request.method == 'POST':
        confirm_pswd = request.POST.get('confirm_pswd', '')
        save = request.POST.get('save', False)
        #... นำค่าไปใช้งานตามต้องการ
        
        form = MemberForm(request.POST)
        #if form.is_valid():
            #form.save()

    else:
        form = MemberForm()

    return render(request, 'member-signin.html', {'form':form})


def pagination_pvnx(request, pg):
    if pg == None:
        pg = 1
        
    rows = Employee.objects.all().order_by('id')
    pgn = Paginator(rows, 2)
    page = pgn.get_page(pg)  
         
    return render(request, 'pagination-pvnx.html', {'page': page})


def pagination_num(request, pg):
    if pg == None:
        pg = 1

    rows = Employee.objects.all().order_by('id')
    pgn = Paginator(rows, 2)
    page = pgn.get_page(pg)  
         
    return render(request, 'pagination-pgnum.html', {'page': page})

def pagination_bs(request, pg):
    if pg == None:
        pg = 1

    rows = Employee.objects.all().order_by('id')
    pgn = Paginator(rows, 2)
    page = pgn.get_page(pg)  
         
    return render(request, 'pagination-bs.html', {'page': page})