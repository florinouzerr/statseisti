from django import forms

#class ContactForm(forms.Form):
#	subject = forms.CharField(max_length=100)
#	envoyeur = forms.EmailField(label="Votre adresse e-mail")
#	message = forms.CharField(widget=forms.Textarea)
#	renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


#https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/les-formulaires-6


# sendemail/forms.py
class ContactForm(forms.Form):
	subject = forms.CharField(label="Sujet",max_length=100,required=True)
	from_email = forms.EmailField(label="Adresse e-mail",required=True)
	message = forms.CharField(label="Message",widget=forms.Textarea, required=True)