from django.shortcuts import render

# Create your views here.

def index(request):
    template='index.html'
    if request.method == "POST":
        print(request.POST["om"])
    context={'cim':"_fodor__"}
    return render(request, template, context)

