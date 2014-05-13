from django.shortcuts import render, HttpResponseRedirect
from siteYoda.core.forms import PadawanForm
from siteYoda.core.models import Padawan

def home(request):
	listPadawans = Padawan.objects.all()
	return render(request, 'inicio.html', {'list': listPadawans})

def cadastrar(request):
	#Esse view está ruim, como posso melhora-lo usando ModelForm???
	if request.method == 'POST':
		form = PadawanForm(request.POST)
		try:
			if form.is_valid():
				obj = Padawan(**form.cleaned_data)
				obj.save()
				return HttpResponseRedirect('/')
			else:
				return render(request, 'cadastro.html', {'form': form})

		except Exception, e:
			form.errors['__all__'] = form.error_class([
				"Erro, existe outro padawan com esse mesmo nome ou email"])
			return render(request, 'cadastro.html', {'form': form})
	else:
		return render(request, 'cadastro.html', {'form':PadawanForm()})