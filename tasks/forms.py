from django import forms
from .models import Task, Solicitud

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complejidad', 'important','subcategoria']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Escribe un titulo' }),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['title', 'description','requerimiento']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Escribe un titulo solicitud' }),
        }