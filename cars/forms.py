
from tkinter.tix import Select
from django import forms

CARS_CHOICES= [
    ('NISSSAN', 'NISSAN'),
    ('MARCEDIES','MARCEDIES'),
    ('POCHE','PORCHE'),
    ('FARRARI', 'FARRARI'),
    ('ROLLS ROYS', 'ROLLS ROYS'),
    ('LAMBORGINI', 'LAMBORGINI')
    ]

class cars(forms.Form):
    manufacturer =  forms.CharField(label='which car you want ?', widget=forms.Select(choices=CARS_CHOICES))
    name = forms.CharField(widget = forms.TextInput) 


