from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'cltvspj/form.html')

def contact(request):
    return render(request, 'cltvspj/contact.html' )
