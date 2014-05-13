# coding: utf-8
from django.test import TestCase
from siteYoda.core.forms import PadawanForm
from siteYoda.core.models import Padawan

class HomeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/')
	
	def test_get(self):
		"""GET / deve retornar o código de status 200."""
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		"""Homepage deve usar o template inicio.html."""
		self.assertTemplateUsed(self.resp, 'inicio.html')

class CadastroTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/cadastrar/')
	
	def test_get(self):
		"""GET / deve retornar o código de status 200."""
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		"""Homepage deve usar o template cadastro.html."""
		self.assertTemplateUsed(self.resp, 'cadastro.html')

	def test_form(self):
		"""O Form deve estar no contexto"""
		form = self.resp.context['form']
		self.assertIsInstance(form, PadawanForm)

class PadawanTest(TestCase):
	def setUp(self):
		self.obj = Padawan(nome='Marcos Dias', raca='humano',
						   email='marcos.dias@email.com.terra.gal',
						   poder=8001, idade=22, sexo='M')

	def test_create(self):
		'Salvar Padawan'
		self.obj.save()
		self.assertEqual(1, self.obj.id)