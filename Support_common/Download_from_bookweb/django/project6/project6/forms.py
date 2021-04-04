from django import forms

class SearchForm(forms.Form):
    search = forms.CharField()


class ProductForm(forms.Form):
    name = forms.CharField(label='ชื่อสินค้า', required=True)
    price = forms.CharField(label='ราคา', required=True)
    color = forms.CharField(label='สี', required=False)
    stock = forms.CharField(label='คงเหลือ', required=False)

    '''
    name = forms.CharField(label='', required=True, widget=forms.TextInput({'placeholder':'ชื่อสินค้า'}))
    price = forms.CharField(label='', required=True, widget=forms.TextInput({'placeholder':'ราคา'}))
    color = forms.CharField(label='', required=False, widget=forms.TextInput({'placeholder':'สี'}))
    stock = forms.CharField(label='', required=False, widget=forms.TextInput({'placeholder':'คงเหลือ'}))
    '''

