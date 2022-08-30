from django import forms
from  .models import *
from django.core.exceptions import ValidationError

class AddSotrForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = None
        self.fields['n_otdela'].empty_label = None

    class Meta:
        model = Sotrudniki
        fields = '__all__'

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) > 25:
            raise ValidationError('Длина фамилии превышает 25 символов ↑')

        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) > 25:
            raise ValidationError('Длина имени превышает 25 символов ↑')

        return first_name

    def clean_otchestvo(self):
        otchestvo = self.cleaned_data['otchestvo']
        if len(otchestvo) > 25:
            raise ValidationError('Длина превышает 25 символов ↑')

        return otchestvo

    def clean_zarplata(self):
        zarplata = self.cleaned_data['zarplata']
        if zarplata > 999999:
            raise ValidationError('Размер зарплаты вышел за границы возможного ↑')

        return zarplata

class AddDogovForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['n_otdela'].empty_label = None

    class Meta:
        model = Dogovor
        fields = '__all__'

    def clean_zakazchik(self):
        zakazchik = self.cleaned_data['zakazchik']
        if len(zakazchik) > 30:
            raise ValidationError('Длина превышает 30 символов ↑')

        return zakazchik

    def clean_number(self):
        number = self.cleaned_data['number']
        if number > 9999999999:
            raise ValidationError('Номер договора вышел за границы возможного ↑')

        return number

class AddProjForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #self.fields['cat'].empty_label = None

    class Meta:
        model = Project
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 30:
            raise ValidationError('Длина превышает 30 символов ↑')

        return name

    def clean_opis(self):
        opis = self.cleaned_data['opis']
        if len(opis) > 100:
            raise ValidationError('Длина описания превышает 100 символов ↑')

        return opis