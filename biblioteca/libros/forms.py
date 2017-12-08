from django import forms

from .models import libro

class LibroModelForm(forms.ModelForm):
    titulo = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Nombre del Libro',
            'class': 'form-control'}))
    autor = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Autor',
            'class': 'form-control'}))
    editorial = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Editorial: ',
            'class': 'form-control'}))
    ISBN = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'ISBN del Libro',
            'class': 'form-control'}))
    precio = forms.FloatField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'Precio',
            'class': 'form-control'}))


    class Meta:
        model = libro
        fields = [
            #"user",
            "titulo", "autor", "editorial", "ISBN",
            "precio"
            ]
