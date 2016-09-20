from django.shortcuts import render

# Create your views here.

def mypost(request):
	return render(request, 'myblog/mypost.html', {})
