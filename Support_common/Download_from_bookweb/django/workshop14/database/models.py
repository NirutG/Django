from django.db import models
from django import forms

# Create your models here.

class Guestbook(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    message = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = '__all__'
        excludes = ['date']
        labels = {
            'name': 'ชื่อ',
            'email': 'อีเมล',
            'phone': 'โทรศัพท์',
            'message': 'ข้อความ'
        }
        widgets = {
            'email': forms.EmailInput(attrs={'required':False}),
            'phone': forms.TextInput(attrs={'required':False}),
			'message': forms.Textarea(attrs={'rows':'3'})
        }
    