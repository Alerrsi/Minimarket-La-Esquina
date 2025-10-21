from django.shortcuts import render, redirect, get_object_or_404
from Login.models import Usuario, Rol
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UsuarioForm, ProfileForm

@login_required
@user_passes_test(lambda x:x.rol.nombre == "Sysadmin")
def Usuarioviews(request):
    if request.user.rol.nombre.strip().lower() == "sysadmin" or request.user.is_staff:
        users = Usuario.objects.all()
        return render(request, 'usuario.html', {'users': users})
    else:
        return redirect("index")

@login_required
@user_passes_test(lambda x:x.rol.nombre == "Sysadmin")
def UsuarioAdd(request):
    if request.user.rol.nombre.strip().lower() == "sysadmin" or request.user.is_staff:
        if request.method == 'POST':
            form = UsuarioForm(request.POST, request.FILES)
            if form.is_valid():
                # Crear usuario
                user_data = form.cleaned_data
                rol = user_data['rol']
                es_sysadmin = rol.nombre.strip().lower() == "sysadmin"
                
                password = user_data.get('password')
                if not password:
                    from django.utils.crypto import get_random_string
                    password = get_random_string(10)

                nuevo_user = Usuario.objects.create_user(
                    nombre=user_data['nombre'],
                    apellido=user_data['apellido'],
                    email=user_data['email'],
                    direccion=user_data['direccion'],
                    rol=rol,
                    password=password
                )
                
                if es_sysadmin:
                    nuevo_user.is_superuser = True
                    nuevo_user.is_staff = True
                    nuevo_user.save()

                messages.success(request, 'Usuario creado exitosamente.')
                return redirect('usuarioViews')
            else:
                # Mostrar errores de validación
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        else:
            form = UsuarioForm()

        roles = Rol.objects.all()
        return render(request, 'form.html', {
            'form': form,
            'roles': roles, 
            'titulo': 'Agregar Usuario',
            'usuario': None
        })
    else: 
        return redirect("index")

@login_required
@user_passes_test(lambda x:x.rol.nombre == "Sysadmin")
def UsuarioMod(request, id):
    if request.user.rol.nombre.strip().lower() == "sysadmin" or request.user.is_staff:
        user = get_object_or_404(Usuario, id=id)

        if request.method == 'POST':
            form = UsuarioForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                user_data = form.cleaned_data
                rol = user_data['rol']
                
                # Actualizar campos básicos
                user.nombre = user_data['nombre']
                user.apellido = user_data['apellido']
                user.email = user_data['email']
                user.direccion = user_data['direccion']
                user.rol = rol

                es_sysadmin = rol.nombre.strip().lower() == "sysadmin"
                user.is_superuser = es_sysadmin
                user.is_staff = es_sysadmin
                
                # Manejar contraseña si se proporciona
                password = user_data.get('password')
                password_changed = False
                
                if password and password.strip():
                    user.set_password(password)
                    password_changed = True

                user.save()
                
                # Si el usuario modificado es el mismo que está logueado, actualizar sesión
                if password_changed and user.id == request.user.id:
                    update_session_auth_hash(request, user)
                    
                messages.success(request, 'Usuario actualizado exitosamente.')
                return redirect('usuarioViews')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        else:
            form = UsuarioForm(instance=user)

        roles = Rol.objects.all()
        return render(request, 'form.html', {
            'form': form,
            'usuario': user, 
            'roles': roles, 
            'titulo': 'Modificar Usuario'
        })
    else: 
        return redirect("index")

@login_required
@user_passes_test(lambda x:x.rol.nombre == "Sysadmin")
def UsuarioDel(request, id):
    if request.user.rol.nombre.strip().lower() == "sysadmin" or request.user.is_staff:
        user = get_object_or_404(Usuario, id=id)
        user.delete()
        return redirect('usuarioViews')
    else:
        return redirect("index")

@login_required

def ViewProfile(request):
    user = request.user
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            
            # Actualizar la sesión si se cambió la contraseña
            password = form.cleaned_data.get('password')
            if password and password.strip():
                update_session_auth_hash(request, user)
                messages.success(request, 'Perfil y contraseña actualizados correctamente.')
            else:
                messages.success(request, 'Perfil actualizado correctamente.')
                
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    
    else:
        form = ProfileForm(instance=user)
    
    context = {
        'user': user,
        'form': form
    }
    return render(request, 'profile.html', context)