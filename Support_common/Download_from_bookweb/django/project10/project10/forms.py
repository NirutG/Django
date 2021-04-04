from django import forms

class UploadForm(forms.Form):
    file = forms.FileField(required=False)

class MultipleUploadForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={'multiple':True}
        )
    )

class UploadImageForm(forms.Form):
    file = forms.ImageField(label='รูปภาพ')


class MultipleUploadFormBS(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'class':'custom-file-input',
                'onchange':'return onFileSelected(this)',
                'multiple':True
            }
        )
    )    
