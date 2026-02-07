from django import forms

from .models import Recipe, Rating, Category


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "description", "image", "categories", "difficulty", "day", "preparation_time", "servings"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Recipe name"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Describe your recipe..."}),
            "image": forms.FileInput(attrs={"class": "form-control", "accept": "image/*"}),
            "categories": forms.CheckboxSelectMultiple(),
            "difficulty": forms.Select(attrs={"class": "form-select"}),
            "day": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "preparation_time": forms.NumberInput(attrs={"class": "form-control", "min": "1"}),
            "servings": forms.NumberInput(attrs={"class": "form-control", "min": "1"}),
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'review']
        widgets = {
            'score': forms.RadioSelect(choices=[(i, f"{i} ★") for i in range(1, 6)]),
            'review': forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Share your thoughts about this recipe (optional)..."}),
        }


