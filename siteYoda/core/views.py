from django.shortcuts import render

def home(request):
	return render(request, 'inicio.html')

def cadastrar(request):
	return render(request, 'cadastro.html')