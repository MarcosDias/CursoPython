# coding: utf-8
from django.test import TestCase

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