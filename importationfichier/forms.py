from django import forms

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50,required=True, widget=forms.TextInput(attrs={'class' : "text-center",'placeholder': "Titre de l'importation"}))
	file = forms.FileField(required=True, widget=forms.FileInput(attrs={'class' : "text-center",}))