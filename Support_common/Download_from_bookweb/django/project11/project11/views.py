from django.shortcuts import render, HttpResponse, redirect, reverse
from .forms import SigninForm
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import random

def index(request):
    return render(request, 'index.html')


def cookie_test(request):
    request.session.set_test_cookie()      
    return render(request, 'cookie-test.html')


def cookie_test_result(request):
    result = request.session.test_cookie_worked()
    if result == True:
        request.session.delete_test_cookie()

    return render(request, 'cookie-test.html', {'result':result})


@csrf_exempt
def cookie_signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            login = request.POST.get('login', '')
            password = request.POST.get('password', '')
            save = request.POST.get('save', False)

            tmp = loader.get_template('cookie-signin.html')
            data = {'form':form}
            response = HttpResponse(tmp.render(data))

            if save:
                response.set_cookie('login', value=login, max_age=60)
                response.set_cookie('password', value=password, max_age=60)
                response.set_cookie('save', value=save, max_age=60)
            else:
                response.delete_cookie('login')
                response.delete_cookie('password')
                response.delete_cookie('save')
            
            return response

    elif 'login' in request.COOKIES:
        login = request.COOKIES.get('login', '')
        password = request.COOKIES.get('password', '')
        save = request.COOKIES.get('save', False)
        form = SigninForm(initial={'login':login, 'password':password, 'save':save})
    else:
        form = SigninForm()
    
    return render(request, 'cookie-signin.html', {'form':form})  


def session_captcha(request):
    if request.method == 'POST':
        post_captcha = request.POST.get('captcha', '')
        msg = '<span style="color:red">ใส่ตัวเลขไม่ถูกต้อง</span>'

        if 'captcha' in request.session:
            if int(post_captcha) == request.session['captcha']:
                msg = 'ใส่ตัวเลขถูกต้อง'
    else:
        msg = ''

    request.session['captcha'] = random.randint(1000, 10000)
    c = request.session['captcha']

    return render(request, 'session-captcha.html', {'msg':msg, 'captcha':c})


def session_signin(request): 
    err_msg = ''
    if request.method == 'POST':
        form = SigninForm(request.POST)
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')

        #ถ้าใส่ค่าถูกต้อง ก็เก็บค่า login ไว้ในเซสชัน
        if login == 'python' and password == 'django':
            request.session['login'] = login
            request.session.set_expiry(0)
        else:
            login = None
            err_msg = 'Login and/or password incorrect'

    #ถ้าเข้าสู่ระบบแล้ว
    elif 'login' in request.session:
        login =  request.session['login']
        form = None
    else:
        form = SigninForm()
        login = None

    return render(request, 'session-signin.html', 
                 {'form':form, 'login':login, 'err_msg':err_msg})


def session_signout(request):
    if 'login' in request.session:
        del request.session['login']
    
    form = SigninForm()
    login = None

    #เมื่อออกจากระบบแล้ว เราต้องย้อนกลับไปที่เพจ signin
    #ดังนั้น จึงควรใช้ฟังก์ชัน redirect() เพื่อให้ URL ที่แสดงบนเบราเซอร์
    #ตรงกับเพจ signin
    return redirect(reverse('signin'), {'form':form, 'login':login})


#ฟังก์ชันที่ใช้เพิ่มชื่อเพจและ URL ลงในเซสชัน
def session_add_rv(request, title, url):
    #ถ้ามีเซสชันที่เก็บข้อมูล Recently Viewed อยู่ก่อนแล้ว
    #ให้อ่านค่ามา ซึ่งจะอยู่ในแบบของดิกชันนารี
    if 'rv' in request.session:
        rv = request.session['rv']
    
    #ถ้ายังไม่มีเซสชันอยู่ก่อน ให้สร้างเป็นดิกชันนารีว่างๆ ขึ้นมาแทน
    else:
        rv = {}

    #ถ้ายังไม่ได้มีเพจนั้นอยู่ในดิกชันารี ให้เพิ่มลงไป
    if title not in rv:
        rv[title] = url
    
    #เก็บดิกชันนารีไว้ในเซสชัน แทนที่ข้อมูลเดิม
    request.session['rv'] = rv

    return rv

#ฟังก์ชันสำหรับเพจแรก แสดงแค่ชื่อรายการบทความ
def session_rv_index(request):
    return render(request, 'session-rv-index.html')

#ฟังก์ชันสำหรับเพจแสดงบทความเรื่อง HTML
def session_rv_html(request):
    #เรียกเมธอด session_add_rv() เพื่อเพิ่มชื่อเพจและ URL ลงในเซสชัน
    #จากนั้นนำผลลัพธ์ ซึ่งก็คือค่าในเซสชัน ส่งไปแสดงผลยังเท็มเพลต
    rv = session_add_rv(request, 'HTML', reverse('rv_html'))
    return render(request, 'session-rv-html.html', {'rv':rv})


def session_rv_css(request):
    rv = session_add_rv(request, 'CSS', reverse('rv_css'))
    return render(request, 'session-rv-css.html', {'rv':rv})


def session_rv_js(request):
    rv = session_add_rv(request, 'JavaScript', reverse('rv_js'))
    return render(request, 'session-rv-js.html', {'rv':rv})


def session_rv_bs(request):
    rv = session_add_rv(request, 'Bootstrap', reverse('rv_bs'))
    return render(request, 'session-rv-bs.html', {'rv':rv})


def session_rv_django(request):
    rv = session_add_rv(request, 'Django', reverse('rv_django'))
    return render(request, 'session-rv-django.html', {'rv':rv})

