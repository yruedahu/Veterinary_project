from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.db import IntegrityError
from .models import User, Client, Veterinarian, Receptionist
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def users_home(request):
    from .models import User
    users = User.objects.all()
    return render(request, 'veterinary_users/users_home.html', {'users': users})

def user_detail_by_username(request, username):
    user = get_object_or_404(User, username=username)

    extra_info = {}

    if user.role == 'client':
        try:
            client = Client.objects.get(user=user)
            extra_info = {
                'type': 'Client',
                'pet_count': client.pet_count
            }
        except Client.DoesNotExist:
            pass

    elif user.role == 'vet':
        try:
            vet = Veterinarian.objects.get(user=user)
            extra_info = {
                'type': 'Veterinarian',
                'license_number': vet.license_number,
                'specialty': vet.specialty,
                'experience': vet.experience_years,
            }
        except Veterinarian.DoesNotExist:
            pass
        

    elif user.role == 'recep':
        try:
            recep = Receptionist.objects.get(user=user)
            extra_info = {
                'type': 'Receptionist',
                'shift': recep.get_shift_display()
            }
        except Receptionist.DoesNotExist:
            pass

    context = {
        'user': user,
        'extra': extra_info,
    }

    return render(request, 'veterinary_users/user_detail.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso. Por favor, elige otro.')
                return render(request, 'veterinary_users/register.html', {'form': form})

            if User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está en uso. Por favor, elige otro.')
                return render(request, 'veterinary_users/register.html', {'form': form})

            try:
                user = form.save(commit=False)
                user.role = request.POST.get('role', 'client')
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone = form.cleaned_data['phone']
                user.address = form.cleaned_data['address']
                user.save()
                messages.success(request, 'Registro exitoso. ¡Bienvenido!')
                return redirect('login')
            except IntegrityError as e:
                print("Error al guardar el usuario:", e)
                messages.error(request, 'Error al registrar el usuario. Intenta con un nombre de usuario diferente.')
        else:
            print("Errores en el formulario:", form.errors)
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CustomUserCreationForm()

    print("Método GET: mostrando formulario de registro")
    return render(request, 'veterinary_users/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'veterinary_users/login.html'

    def form_valid(self, form):
        user = form.get_user()
        print(f"Usuario autenticado: {user.username}, Rol: {user.role}")
        if user.role == 'admin':
            messages.success(self.request, 'Inicio de sesión exitoso. ¡Bienvenido, administrador!')
            return redirect('admin_users')
        messages.success(self.request, 'Inicio de sesión exitoso. ¡Bienvenido!')
        return redirect('users_home')

    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)

@login_required
def admin_users(request):
    # Solo usuarios autenticados pueden acceder
    user = request.user
    print(f"Usuario actual: {getattr(user, 'username', 'Anonimo')}, Rol: {getattr(user, 'role', 'Sin rol')}")
    if not hasattr(user, 'role') or user.role != 'admin':
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('login')
    return render(request, 'veterinary_users/admin_users.html')

def user_edit(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('users_home')
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'veterinary_users/user_edit.html', {'form': form, 'user': user})


def user_delete(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        if user.id is None:
            messages.error(request, 'No se puede eliminar este usuario porque su ID es inválido.')
            return redirect('users_home')
        user.delete()
        messages.success(request, 'Usuario eliminado correctamente.')
        return redirect('users_home')
    return render(request, 'veterinary_users/user_confirm_delete.html', {'user': user})

def veterinarios(request):
    return render(request, 'veterinary_users/veterinarios.html')

def citas(request):
    return render(request, 'veterinary_users/citas.html')

def mascotas(request):
    return render(request, 'veterinary_users/mascotas.html')

def ajustes(request):
    return render(request, 'veterinary_users/ajustes.html')
