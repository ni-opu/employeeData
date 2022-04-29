from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.
def addShow(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            employee_id = form.cleaned_data['employee_id']
            shift = form.cleaned_data['shift']
            arrival = form.cleaned_data['arrival']
            remark = form.cleaned_data['remark']
            reg = Todo(name=name, employee_id=employee_id, shift=shift, arrival=arrival, remark=remark)
            reg.save()
            return HttpResponseRedirect('/') # this prevent resubmittion upon refresh
            form = TodoForm()
    else:
        form = TodoForm()
    todoList = Todo.objects.all()
    return render(request, 'employeeData/addShowStudent.html', {'form':form, 'todoList':todoList})

def updateData(request, id):
    if request.method == 'POST':
        data = Todo.objects.get(pk=id)
        form = TodoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:
        data = Todo.objects.get(pk=id)
        form = TodoForm(instance=data)
    todoList = Todo.objects.all()
    return render(request, 'employeeData/addShowStudent.html', {'uform':form, 'todoList':todoList})

def deleteData(request, id):
    if request.method == 'POST':
        item = Todo.objects.get(pk=id)
        item.delete()
        return HttpResponseRedirect('/')
