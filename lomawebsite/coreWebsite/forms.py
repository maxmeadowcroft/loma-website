from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name",
            "style": "background-color: rgba(255, 255, 255, 0.2); border: none; border-bottom: 2px solid #8a1538; border-radius: 0; margin-bottom: 15px;"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Your Email",
            "style": "background-color: rgba(255, 255, 255, 0.2); border: none; border-bottom: 2px solid #8a1538; border-radius: 0; margin-bottom: 15px;"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Your Message",
            "rows": 5,
            "style": "background-color: rgba(255, 255, 255, 0.2); border: none; border-bottom: 2px solid #8a1538; border-radius: 0; margin-bottom: 15px;"
        })
    )
