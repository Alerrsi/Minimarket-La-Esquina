from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "index.html")

@login_required
def direct(request):
    if hasattr(request.user, 'rol') and request.user.rol:
        if request.user.rol.nombre.strip().lower() == "sysadmin" or request.user.is_staff:
            return redirect("usuario")
    
    return redirect("index")