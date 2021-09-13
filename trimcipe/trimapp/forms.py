from django import forms

class TrimRecipe(forms.Form):
    url = forms.URLField(widget=forms.URLInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'What\'s the URL of your recipe?',
            'aria-label' : 'Recipe URL',
            'aria-describedby' : 'button-addon2'
        }
    ))
