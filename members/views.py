from django.shortcuts import render, redirect, HttpResponse
from . forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'members/about.html')


def service(request):
    if request.method == "POST":
        forms = ServiceForm(request.POST, request.FILES)
        if forms.is_valid():
            service = forms.save(commit=False)
            service.created_by = request.user
            service.save()
            return redirect('home')
        return redirect('service')
    return render(request, 'members/service.html')


def service_list(request):
    services = Service.objects.all()
    return render(request, 'members/service-list.html', {'services': services})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('contact')
        
    return render(request, 'members/contact.html')

def contact_list(request):
    contacts = Contact.objects.all()
    context = {"contact_list": contacts}
    return render(request, 'members/contact_list.html', context)


def contact_edit(request, pk):
    contact = Contact.objects.get(pk=pk)
    forms = ContactForm(request.POST or None, instance=contact)
    if forms.is_valid():
        forms.save()
        return redirect('contact-list')
    return render(request, 'members/contact_edit.html', {'forms': forms})


def contact_delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return HttpResponse('successfully deleted.')


def feedback(request):
    return render(request, 'members/feedback.html')


#function based view for todo application
def task(request):
    print(request.POST)
    if request.method == 'POST':
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()

        else:
            return render(request, 'todos/task.html')
        
    return render(request, 'todos/task.html')


def task_list(request):
    tasks = Task.objects.filter(is_completed=False)
    return render(request, 'todos/task_list.html', {'tasks': tasks})


def edit_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        forms = TaskForm(request.POST or None, instance=task)
        if forms.is_valid():
            forms.save()
            return redirect('task-list')

        else:
            return render(request, 'todos/edit_task.html', {'forms': forms})
        
    forms = TaskForm(instance=task)
        
    return render(request, 'todos/edit_task.html', {'forms': forms})


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return HttpResponse('successfully deleted.')


def completed_task(request):
    tasks = Task.objects.filter(is_completed=True)
    return render(request, 'todos/completed_task.html', {'tasks': tasks})
        



