from django.shortcuts import render
#from django.shortcuts import render  
from django.http import HttpResponse  
from .functions import handle_uploaded_file 
from .forms import UploadFileForm  
def upload_file(request):  
    if request.method == 'POST':  
        form = UploadFileForm(request.POST, request.FILES)  
        if form.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        form = UploadFileForm()  
        return render(request,"upload_file.html",{'form':form})  
# Create your views here.
