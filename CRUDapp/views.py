from django.shortcuts import render, redirect
from .models import StudentDetails
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')
def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        mail = request.POST['mail']
        gender = request.POST['gender']
        phnumber = request.POST['phnumber']
        print(name, age, mail)
        obj = StudentDetails()
        obj.name = name
        obj.age = age
        obj.mail = mail
        obj.gender = gender
        obj.phnumber = phnumber
        obj.save()
        return redirect('/form')
    return render(request, 'form.html')
def display(request):
    obj = StudentDetails.objects.all()
    return render(request, 'display.html', {'obj':obj})
def update(request, id):
    obj = StudentDetails.objects.get(id=id)
    if request.method == 'POST':
        up_name = request.POST['up_name']
        up_age = request.POST['up_age']
        up_mail = request.POST['up_mail']
        up_gender = request.POST['up_gender']
        up_phnumber = request.POST['up_phnumber']
        obj.name = up_name
        obj.age = up_age
        obj.mail = up_mail
        obj.gender = up_gender
        obj.phnumber = up_phnumber
        obj.save()
        return redirect('/display')
    return render(request, 'update.html', {'obj':obj})
def delete(request, id):
    obj = StudentDetails.objects.get(id = id)
    obj.delete()
    return redirect('/display')
    return render(request, 'display.html')
        