from django import forms

class SearchForm(forms.Form):
    searchbBox = forms.CharField(
        label='Search', 
        widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'Paste Youtube link here'})
    )