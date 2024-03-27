from django.shortcuts import render

def about(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request,'about.html',{'name':name,'email':email,'select':select})
    else:
        return render(request,'about.html')

        




def submit_form(request):
    return render(request, 'form.html')  
