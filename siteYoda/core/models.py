# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

SEXO = (('M', 'M'),
		('F', 'F'))

RACAS = (('Humano', 'Humano'),
    	 ('Rwook', 'Rwook'),
    	 ('Povo da Areia', 'Povo da Areia'))

class Padawan(models.Model):
	nome = models.CharField(_('Nome'), max_length=100, unique=True)
	raca = models.CharField(_('Raça'), max_length=50, choices=RACAS)
	email = models.EmailField(_('Email'), unique=True)
	poder = models.IntegerField(_('Midi-chlorians (Poder)'), null=True)
	idade = models.IntegerField(_('Idade'), null=True)
	sexo = models.CharField(_('Sexo'), choices=SEXO, max_length=1)
	
	def __unicode__(self):
		return self.nome