from django.http import Http404
from django.shortcuts import render
from .models import Exhibition

def index(request):
	return render(request, 'web/base.html')

def about(request):
	return render(request, 'web/about.html')	

def phad(request):
	return render(request, 'web/phad.html')

def phadmaking(request):
	return render(request, 'web/phadmaking.html')

def phadperfomance(request):
	return render(request, 'web/phadperfomance.html')

def contact(request):
	return render(request, 'web/contact.html')	

def awards(request):
	return render(request, 'web/awards.html')

def blog(request):
	allexhibitions = Exhibition.objects.all()
	context = {
		'allexhibitions' : allexhibitions,
	}
	return render(request, 'web/blog.html',context)	