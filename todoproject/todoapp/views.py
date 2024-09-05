from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . models import Task
from . forms import ToDoForm

from django . views.generic import ListView
from django . views.generic.detail import DetailView
from django . views.generic.edit import UpdateView,DeleteView


#Using Class Generic Views


class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'  #itertaive variable in for loop


class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'updateview.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    
    def get_success_url(self):
        return reverse_lazy('classdetailview', kwargs = {'pk': self.object.id})
    
class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('classlisthome')


# Create your views here.


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':

        name = request.POST.get('task', '')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')

        task = Task(name = name, priority = priority, date = date)
        task.save()
       
    return render(request, 'home.html',{'task1' : task1})




# def details(request):
   
#     return render(request , 'details.html',)

def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST' :
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request,id):
    task = Task.objects.get(id = id)
    forms = ToDoForm(request.POST or None, instance=task)
    if forms.is_valid():
        forms.save()

        return redirect('/')
    return render(request,'update.html',{'forms':forms, 'task':task})