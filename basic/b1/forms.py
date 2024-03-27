from django import forms

class contactForm(forms.Form):
    name=forms.CharField(label="ENter Your Name")
    email=forms.EmailField(label="Enter your email")
    