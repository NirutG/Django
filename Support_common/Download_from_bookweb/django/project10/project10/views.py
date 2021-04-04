from django.shortcuts import render
from .forms import *
from database.models import *
import os
import random
from PIL import Image 
from io import BytesIO


def index(request):
    return render(request, 'index.html')



def upload_basic(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
        else:
            file = None
    else:
        form = UploadForm()
        file = None

	#ส่งออบเจ็กต์หรืออินสแตนซ์ของ UploadedFile ไปยังเท็มเพลตร่วมกับฟอร์ม
	#เพื่อแสดงข้อมูลของไฟล์ที่อัปโหลดขึ้นไป
    return render(request, 'upload-basic.html', 
				{'form':form, 'file':file})




'''
def upload_basic(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            #เปิดไฟล์ในโฟลเดอร์ media ตามที่ได้สร้างเอาไว้ โดยใช้ชือเดียวกับไฟล์ที่อัปโหลดขึ้น
            #เพื่อเขียน (w) ในโหมดไบนารี (b) ถ้ายังไม่มีอยู่ก่อน ให้สร้างขึ้นใหม่ (+)
            with open(f'media/upload/{file.name}', 'wb+') as target:
                #แบ่งไฟล์เป็นส่วนย่อยๆ แล้วนำมาเขียนลงในไฟล์เป้าหมายต่อเนื่องกันจนครบ
                for chunk in file.chunks():
                    target.write(chunk)

                #หรืออ่านเนื้อหาของไฟล์ทั้งหมด แล้วเขียนพร้อมกันทีเดียว
                #โดยไม่ต้องใช้ลูป for แต่ไม่ควรกับไฟล์ที่มีขนาดใหญ่
                #target.write(f.read())

		else:
			file = None

    else:
        form = UploadForm()
        file = None
    
    return render(request, 'upload-basic.html', {'form':form, 'file':file})
'''


'''
def upload_basic(request):
    if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			file = request.FILES['file']
			#ถ้ามีไฟล์ชื่อนั้นอยู่ก่อนแล้ว
			if os.path.exists(f'media/upload/{file.name}'):
				sp = file.name.split('.', 1)
				name = sp[0]
				ext = sp[1]
				#ควรให้ช่วงของการสุ่มตัวเลขห่างกันมากพอสมควร
 				#มิฉะนั้นก็มีโอกาสได้เลขที่นำไปต่อท้ายแล้วซ้ำกับชื่อไฟล์เดิม
				r = random.randint(1000, 10000)
				file.name = f'{name}_{r}.{ext}'	#เปลี่ยนชื่อไฟล์

			with open(f'media/upload/{file.name}', 'wb+') as target:
				for chunk in file.chunks():
					target.write(chunk)

		else:
			file = None
    else:
		form = UploadForm()
		file = None
    
	return render(request, 'upload-basic.html', {'form':form, 'file':file})	
'''


def get_unique_name(dir, filename):
    if not dir.endswith('/'):
        dir += '/'
    
    if os.path.exists(f'{dir}{filename}'):
        sp = filename.split('.', 1)
        name = sp[0]
        ext = sp[1]
        r = random.randint(1000, 10000)
        return f'{name}_{r}.{ext}'
    else:
        return filename


def save_file(dir, file):
    if not dir.endswith('/'):
        dir += '/'

    with open(f'{dir}{file.name}', 'wb+') as target:
        for chunk in file.chunks():
            target.write(chunk)

'''
def upload_basic(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid() and 'file' in request.FILES:
            file = request.FILES['file']
            filename = get_unique_name('media/upload', file.name)
            file.name = filename
            save_file('media/upload/', file)
        else:
            file = None

    else:
        form = UploadForm()
        file = None
    
    return render(request, 'upload-basic.html', {'form':form, 'file':file})	
'''

def upload_multiple(request):
    if request.method == 'POST':
        form = MultipleUploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            for (i, f) in enumerate(files):
                filename = get_unique_name('media/upload/', f.name)
                f.name = filename
                save_file('media/upload/', f)
                files[i].name = filename

            fs = files

        else:
            fs = None

    else:
        form = MultipleUploadForm()
        fs = None
    
    return render(request, 'upload-multiple.html', {'form':form, 'files':fs})


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']
            file.name = get_unique_name('media/upload/', file.name)
            save_file('media/upload/', file)

        else:
            file = None
    else:
        form = UploadImageForm()
        file = None

    return render(request, 'upload-image.html', {'form':form, 'file':file})


def upload_image_resize(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            bio = BytesIO(file.read())
            img = Image.open(bio)
            max_size = (480, 640)
            img.thumbnail(max_size, Image.ANTIALIAS)
            
            file.name = get_unique_name('media/upload/', file.name)
 
            img.save(f'media/upload/{file.name}', file.image.format, quality=95)
            file.image = Image.open(f'media/upload/{file.name}')

        else:
            file = None

    else:
        form = UploadImageForm()
        file = None

    return render(request, 'upload-image-resize.html', {'form':form, 'file':file})


def upload_model(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['profile']
            Member.file_format = file.image.format
            Member.file_name = file.name
            Member.content_type = file.content_type
            form.save()

        else:
            file = None

    else:
        form = MemberForm()
        file = None
        
    data = Member.objects.all()
    return render(request, 'upload-model.html', {'form':form, 'data':data})


def upload_model_multiple(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            files = request.FILES.getlist('files')
            pd = form.save()    #pd เป็นออบเจ็กต์ผลลัพธ์ของเมธอด save()

            #อ่านค่า id ของสินค่า ที่เพิ่มใหม่
            #เพื่อนำไปเติมลงในโมเดล ProductImage
            pid = pd.id         
            
            #เนื่องจากเราอัปโหลดแบบ multiple 
            #จึงต้องใช้ลูปเพื่อบันทึกข้อมูลตามจำนวนไฟล์
            #แต่เราไม่ได้สร้าง โมเดลฟอร์ม ของ ProductImage
            #ดังนั้น จึงต้องเพิ่มข้อมูลแบบกำหนดค่าให้แก่โมเดลโดยตรง
            for f in files:
                pd_img = ProductImage(product_id=pid, image_file=f)

                #กำหนดข้อมูลของภาพให้แก่แอตทริบิวต์ในคลาส ProductImage
                #เพื่อใช้ในการเปลี่ยนขนาดของภาพ
                pd_img.file_format = f.content_type.split('/')[1]
                pd_img.file_name = f.name
                pd_img.content_type = f.content_type
                pd_img.save()

    else:
        form = ProductForm()
     
    product = Product.objects.all()     #ข้อมูลสินค้าแต่ละชนิด
    images = ProductImage.objects.all() #ข้อมูลตำแหน่งภาพ

    return render(request, 'upload-model-multiple.html', 
                  {'form':form, 'product':product, 'images':images})
