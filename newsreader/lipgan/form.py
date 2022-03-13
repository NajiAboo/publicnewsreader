from django import forms

class TextForm(forms.Form):
    txtArea = forms.Textarea()

