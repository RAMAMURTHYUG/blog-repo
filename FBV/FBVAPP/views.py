from django.shortcuts import render,redirect
from FBVAPP.models import Employee
from FBVAPP.forms import EmployeeForm
def display(request):
    e=Employee.objects.all().order_by('eno')
    d={"emp":e}
    return render(request,"templateapp/index.html",d)
def insert_view(request):
    f=EmployeeForm()
    if request.method=="POST":
        f=EmployeeForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect("/")
    d={'form':f}
    return render(request,"templateapp/insert.html",d)
def delete_view(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect("/")
def update_view(request,id):
    e=Employee.objects.get(id=id)
    if request.method=="POST":
        f=EmployeeForm(request.POST,instance=e)
        if f.is_valid():
            f.save(commit=True)
        return redirect("/")
    d={"emp":e}
    return render(request,"templateapp/update.html",d)

# Create your views here.
