from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm, SolicitudForm
from .models import Task, Solicitud
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'La contraseña no es correcta'
        })

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {'tasks' : tasks})

@login_required
def solicitudes(request):
    solicitudes = Solicitud.objects.filter(user=request.user)
    return render(request, 'solicitudes.html', {'solicitudes' : solicitudes})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {'tasks' : tasks})

@login_required
def solicitudes_completed(request):
    solicitudes = Solicitud.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'solicitudes.html', {'solicitudes' : solicitudes})

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': "Error updating task"})

@login_required
def solicitud_detail(request, solicitud_id):
    if request.method == 'GET':
        solicitud = get_object_or_404(Task, pk=solicitud_id, user=request.user)
        form = SolicitudForm(instance=solicitud)
        return render(request, 'solicitud_detail.html', {'task': solicitud, 'form': form})
    else:
        try:
            solicitud = get_object_or_404(Solicitud, pk=solicitud_id, user=request.user)
            form = SolicitudForm(request.POST, instance=solicitud)
            form.save()
            return redirect('solicitudes')
        except ValueError:
            return render(request, 'solicitud_detail.html', {'solicitud': solicitud, 'form': form, 'error': "Error updating task"})
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task,pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def complete_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud,pk=solicitud_id, user=request.user)
    if request.method == 'POST':
        solicitud.datecompleted = timezone.now()
        solicitud.save()
        return redirect('solicitudes')

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

@login_required
def delete_solicitud(request,solicitud_id):
    solicitud = get_object_or_404(Task,pk=solicitud_id, user=request.user)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('solicitudes')

@login_required
def create_task(request):
    if request.method =='GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error' : ' Please provide valide data'
            })

@login_required
def create_solicitud(request):
    if request.method =='GET':
        return render(request, 'create_solicitud.html', {
            'form': SolicitudForm
        })
    else:
        try:
            form = SolicitudForm(request.POST)
            new_solicitud = form.save(commit=False)
            new_solicitud.user = request.user
            new_solicitud.save()
            return redirect('solicitudes')
        except ValueError:
            return render(request, 'create_solicitud.html', {
                'form': SolicitudForm,
                'error' : ' Please provide valide data'
            })

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')