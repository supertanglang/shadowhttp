from django import forms

class AddWorldConfForm(forms.Form):
    domain = forms.CharField(label='Domain', max_length=200)

