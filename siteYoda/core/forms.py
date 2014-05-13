# coding: utf-8
from django import forms

RACAS = (('Humano', 'Humano'),
    	 ('Rwook', 'Rwook'),
    	 ('Povo da Areia', 'Povo da Areia'))

SEXO = (('M', 'M'),
	 	('F', 'F'))

class PadawanForm(forms.Form):
	nome = forms.CharField(label='Nome')
	raca = forms.ChoiceField(label='Raça', choices=RACAS)
	email = forms.EmailField(label='Email')
	poder = forms.IntegerField(label='Midi-chlorians (Poder)', required=False)
	idade = forms.IntegerField(label='Idade', required=False)
	sexo = forms.ChoiceField(label='Sexo', choices=SEXO, widget=forms.RadioSelect)
