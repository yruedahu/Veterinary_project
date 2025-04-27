from django.shortcuts import render, get_object_or_404
from .models import User, Client, Veterinarian, Receptionist

def users_home(request):
    return render(request, 'veterinary_users/users_home.html')

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
