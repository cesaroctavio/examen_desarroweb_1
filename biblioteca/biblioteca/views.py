from django.shortcuts import render

def home(request):
    print request
    v = "mi variable"
    v2 = {"Usuario: ":"Jose Luis"}
    v3 = {"Usuario: ":"Cesar"}
    return render(request, "home.html", {'v':v, 'v2':v2, 'v3':v3,})
