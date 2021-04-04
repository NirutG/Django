from django import forms

class SigninForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    save = forms.BooleanField(required=False)

'''
class AccountForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class AddressForm(forms.Form):
    address1 = forms.CharField()
    address2 = forms.CharField()

class PaymentForm(forms.Form):
    c = [('Bank Transfer', 'Bank Transfer'), ('Credit Card', 'Credit Card'), ('COD', 'COD')]
    payment = forms.ChoiceField(
        choices=c,
        widget=forms.RadioSelect()
    )
'''