from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from users.models import CustomUser


@csrf_exempt  # Only use this decorator during development/testing
def register(request):
    if request.method == 'POST':
        try:
            # Parse the request body
            data = json.loads(request.body)

            # Check if passwords match
            if data.get('password') != data.get('confirm_password'):
                return JsonResponse({'error': 'Passwords do not match'}, status=400)

            user_type = data.get('user_type', 'user')  # Default to 'user' if not provided
            if user_type not in ['user', 'admin']:
                return JsonResponse({'error': 'Invalid user type'}, status=400)

            # Create the user
            user = get_user_model().objects.create(
                username=data.get('username'),
                password=make_password(data.get('password')),
                user_type=user_type
            )

            return JsonResponse({'message': f'{user.user_type} registered successfully!'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return JsonResponse({'message': f'Logged in as {user.username}'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)


def get_admins(request):
    admins = CustomUser.objects.filter(user_type='admin')
    admin_data = [{'id': admin.id, 'username': admin.username} for admin in admins]
    return JsonResponse(admin_data, safe=False, status=200)
