from django.http import request
from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')


def Guide(request):
    return render(request, 'guide.html')

def GuideTf(request):
    return render(request, 'guide_tf.html')

def Amputation(request):
    return render(request, 'core/amputation.html')

def GuideTt(request):
    return render(request, 'guide_tt.html')

def Search(request):
    return render(request, 'core/search.html')
    
def UserStory(request):
    return render(request, 'core/userstory.html')

def AdminPage(request):
    return render(request, 'core/adminpage.html')