from django.shortcuts import render
from  .forms import contactForm
def home(request):
    return render(request, 'base.html')


def submit_form(request):
    return render(request,'b1/form.html')

def DjangoForm(request):
    form=contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,"b1/django_form.html")    