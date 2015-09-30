from django import forms
from myapp.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        # fields = ['first','middle','last']
        fields = '__all__'

