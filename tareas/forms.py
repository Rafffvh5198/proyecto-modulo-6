from django import forms
from .models import Proyecto, Tarea
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})
        
class ProyectoForm(forms.ModelForm):
    
    class Meta:
        model = Proyecto
        fields = ['nombre','descripcion']
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo','descripcion','completada']       
        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        
        for field in self.fields.values():
            field.help_text = None
