from django import forms

from .models import libro

class LibroModelForm(forms.ModelForm):

    class Meta:
        model = libro
        fields = [
            #"user",
            "titulo", "autor", "editorial", "ISBN",
            "precio"
            ]
