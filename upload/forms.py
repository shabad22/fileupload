from django import forms  
class UploadFileForm(forms.Form): 
    file = forms.FileField() # for creating file input
