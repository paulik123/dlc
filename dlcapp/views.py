from django.shortcuts import render

def index(request):
	context = {}

	return render(request, 'dlcapp/index.html', context)