from django.db import models
from django import forms
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.

'''
class Member(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=10)
    profile = models.ImageField(upload_to='profile/', default='profile/user.png')
'''

class Member(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=10)
    profile = models.ImageField(upload_to='profile/', default='profile/user.png')

    #แอตทริบิวต์ที่จะรับข้อมูลเพิ่มเติมจากวิว
    #ซึ่งควรกำหนดค่าดีฟอลต์เอาไว้ด้วย
    file_format = 'JPEG'
    file_name = 'unnamed.jpg'
    content_type = 'image/jpeg'

    #โอเวอร์ไรด์เมธอด save()
    def save(self, *args, **kwargs):
        if self.profile:
            bio = BytesIO(self.profile.read())
            img = Image.open(bio)
            max_size = (120, 120) 
            img.thumbnail(max_size, Image.ANTIALIAS)

            buffer = BytesIO()
            img.save(buffer, self.file_format, quality=95)
            buffer.seek(0)

            self.profile = InMemoryUploadedFile(
                buffer,
                'ImageField', 
                self.file_name,
                self.content_type,
                buffer.__sizeof__,
                None
            )

        super(Member, self).save(*args, **kwargs)

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()


class ProductForm(forms.ModelForm):
    files = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple':True})
    )

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name':'Product Name'
        }


class ProductImage(models.Model):
    product_id = models.PositiveIntegerField()
    image_file = models.ImageField(upload_to='product/')

    #แอตทริบิวต์เก็บข้อมูลเพิ่มเติม ไม่ใช่ฟิลด์
    file_format = 'JPEG'
    file_name = 'unnamed.jpg'
    content_type = 'image/jpeg'

    def save(self, *args, **kwargs):
        if self.image_file:
            bio = BytesIO(self.image_file.read())
            img = Image.open(bio)
            max_size = (480, 640)

            img.thumbnail(max_size, Image.ANTIALIAS)
            buffer = BytesIO()
            img.save(buffer, self.file_format, quality=95)
            buffer.seek(0)
            self.image_file = InMemoryUploadedFile(
                buffer,
                'ImageField', 
                self.file_name,
                self.content_type,
                buffer.__sizeof__,
                None
            )

        super(ProductImage, self).save(*args, **kwargs)
