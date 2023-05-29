from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'poorna','age':'21'}
    return render(request,'wish.html',context=d)