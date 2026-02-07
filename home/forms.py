from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["day", "name", "description", "preparation_time", "servings"]
        widgets = {
            "day": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "preparation_time": forms.NumberInput(attrs={"class": "form-control"}),
            "servings": forms.NumberInput(attrs={"class": "form-control"}),
        }


