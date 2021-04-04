from django import forms

class CharFieldForm(forms.Form):
    login = forms.CharField(
        label='',
        required=False,
        max_length=20,
        min_length=4,
        widget=forms.TextInput(attrs={
            'placeholder': 'Login',
            'size': '20'
        })
    )

    pswd = forms.CharField(
		label='',
        required=False,
		max_length='10',
		min_length='4',
		widget=forms.PasswordInput(attrs={
			'placeholder': 'รหัสผ่าน',
			'size': '20',
		})
	)
    
    memo = forms.CharField(
        label='',
        required=False,
        max_length=150,
        widget=forms.Textarea(attrs={
            'placeholder': 'บันทึกช่วยจำ',
            'cols': '30',
            'rows': '3'
        })
    )


class NumberForm(forms.Form):
    quantity = forms.IntegerField(
        label='จำนวน',
        required=False,
        min_value=1,
        max_value=10,
        widget=forms.NumberInput()
    )

    price = forms.FloatField(
        label='ราคา',
        min_value=1,
        required=False       
    )


class EmailURLForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=False,
    )

    website = forms.URLField(
        label='Website',
        required=False,
        widget=forms.URLInput(attrs={
            'size': 40
        })
    )


class BooleanForm(forms.Form):
    save = forms.BooleanField(
        label='จัดเก็บข้อมูลไว้ในเครื่องนี้',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'value': 'Save',
            'checked': False
        })
    )


class ChoiceForm(forms.Form):
    ch_colors = [('#ff0000', 'Red'), ('#00ff00', 'Green'), ('#0000ff', 'Blue')]

    color = forms.ChoiceField(
        choices=ch_colors,
        label='Color',
        required=False,
        widget=forms.RadioSelect
    )

    ch_styles = [('<b>', 'Bold'), ('<i>', 'Italic'), ('<u>', 'Underline')]

    font_style = forms.MultipleChoiceField(
        choices=ch_styles, 
        label='Font Style',
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    
    ch_sizes =[('14px', 'Small'), ('16px', 'Medium'), ('20px', 'Large')]

    font_size = forms.ChoiceField(
        choices=ch_sizes,
        label='Font Size',
        required=False,
        widget=forms.Select
    )

    ch_families = [('Tahoma', 'Tahoma'), ('Arial', 'Arial'), 
                    ('Times New Roman', 'Times New Roman'), 
                    ('Microsoft Sans Serif', 'Microsoft Sans Serif')]

    font_family = forms.MultipleChoiceField(
        label='Font Family',
        choices=ch_families,
        required=False,
        widget=forms.SelectMultiple, 
    )


class DateAndTimeForm(forms.Form):
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type':'date'})
    )

    time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={'type':'time'})
    )


class CrispyForm(forms.Form):
    text = forms.CharField(
        required=False
    )

    textarea = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 2
        })
    )

    radio = forms.ChoiceField(
        choices=[(1, 'One'), (2, 'Two'), (3, 'Three')],
        required=False,
        widget=forms.RadioSelect()
    )

    checkbox = forms.MultipleChoiceField(
        choices=[(4, 'Four'), (5, 'Five'), (6, 'Six')],
        required=False,
        widget=forms.CheckboxSelectMultiple()
    )

    select = forms.ChoiceField(
        choices=[(7, 'Seven'), (8, 'Eight'), (9, 'Nine')],
        required=False,
        widget=forms.Select()
    ) 