from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request=request,
                  template_name="dashboard/menu.html",)
                  #context={"login": user_login.objects.all})
