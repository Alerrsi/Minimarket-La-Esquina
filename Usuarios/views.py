from django.shortcuts import render, redirect, get_object_or_404
from Login.models import Usuario, Rol
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def Usuarioviews(request):
    if request.user.rol.nombre.strip().lower() == "sysadmin" or request.user.is_staff:
        users = Usuario.objects.all()
        return render(request, 'usuario.html', {'users': users})
    else:
        return redirect("direct")

@login_required
def UsuarioAdd(request):
    if request.user.rol.nombre.strip().lower() == "sysadmin" or request.user.is_staff:
        if request.method == 'POST':
            nombre = request.POST.get('nombre').capitalize()
            apellido = request.POST.get('apellido').capitalize()
            email = request.POST.get('email')
            direccion = request.POST.get('direccion')
            rol_id = request.POST.get('rol')

            rol = Rol.objects.get(id=rol_id)
            es_sysadmin = rol.nombre.strip().lower() == "sysadmin"

            password = request.POST.get('password')
            if not password:
                from django.utils.crypto import get_random_string
                password = get_random_string(10)

            nuevo_user = Usuario.objects.create_user(
                nombre=nombre,
                apellido=apellido,
                email=email,
                direccion=direccion,
                rol=rol,
                password=password
            )
            
            if es_sysadmin:
                nuevo_user.is_superuser = True
                nuevo_user.is_staff = True
                nuevo_user.save()

            return redirect('usuario')

        roles = Rol.objects.all()
        return render(request, 'form.html', {
            'roles': roles, 
            'titulo': 'Agregar Usuario',
            'usuario': None
        })
    else: 
        return redirect("direct")

@login_required
def UsuarioMod(request, id):
    if request.user.rol.nombre.strip().lower() == "sysadmin" or request.user.is_staff:
        user = get_object_or_404(Usuario, id=id)

        if request.method == 'POST':
            user.nombre = request.POST.get('nombre').capitalize()
            user.apellido = request.POST.get('apellido').capitalize()
            user.email = request.POST.get('email')
            user.direccion = request.POST.get('direccion')
            rol_id = request.POST.get('rol')
            rol = Rol.objects.get(id=rol_id)
            user.rol = rol

            es_sysadmin = rol.nombre.strip().lower() == "sysadmin"
            user.is_superuser = es_sysadmin
            user.is_staff = es_sysadmin
            
            password = request.POST.get('password')
            if password:
                user.set_password(password)

            user.save()
            return redirect('usuario')

        roles = Rol.objects.all()
        return render(request, 'form.html', {
            'usuario': user, 
            'roles': roles, 
            'titulo': 'Modificar Usuario'
        })
    else: 
        return redirect("direct")

@login_required
def UsuarioDel(request, id):
    if request.user.rol.nombre.strip().lower() == "sysadmin" or request.user.is_staff:
        user = get_object_or_404(Usuario, id=id)
        user.delete()
        return redirect('usuario')
    else:
        return redirect("direct")
    
@login_required
def ViewProfile(request):
    # El usuario ya está autenticado gracias al decorator @login_required
    user = request.user
    
    if request.method == 'POST':
        # Actualizar datos del perfil
        user.nombre = request.POST.get('nombre', user.nombre)
        user.apellido = request.POST.get('apellido', user.apellido)
        user.email = request.POST.get('email', user.email)
        user.direccion = request.POST.get('direccion', user.direccion)
        
        # Manejar cambio de contraseña si se proporciona
        password = request.POST.get('password')
        if password:
            user.set_password(password)
        
        user.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('profile')
    
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)