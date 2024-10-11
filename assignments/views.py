from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from users.models import CustomUser
from .models import Assignment
from django.contrib.auth.decorators import login_required
import json

@csrf_exempt
@login_required
def upload_assignment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Fetch the user who is uploading the assignment based on the userId
            user = get_object_or_404(CustomUser, username=data['userId'], user_type='user')

            # Fetch the admin to whom the assignment is tagged based on the admin name
            admin = get_object_or_404(CustomUser, username=data['admin'], user_type='admin')

            # Create the assignment object
            assignment = Assignment.objects.create(
                user=user,
                task=data['task'],
                admin=admin,
            )

            return JsonResponse({'message': 'Assignment uploaded successfully!'}, status=201)

        except KeyError:
            return JsonResponse({'error': 'Invalid data format or missing fields.'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid HTTP method.'}, status=405)
@login_required
def view_assignments(request):
    if request.user.user_type == 'admin':
        assignments = Assignment.objects.filter(admin=request.user)
        data = [
            {
                'id': a.id,
                'user': a.user.username,
                'task': a.task,
                'timestamp': a.timestamp,
                'status': a.status
            }
            for a in assignments
        ]
        return JsonResponse(data, safe=False, status=200)

@csrf_exempt
@login_required
def manage_assignment(request, assignment_id, action):
    try:
        assignment = Assignment.objects.get(id=assignment_id, admin=request.user)
        if action == 'accept':
            assignment.status = 'accepted'
        elif action == 'reject':
            assignment.status = 'rejected'
        assignment.save()
        return JsonResponse({'message': f'Assignment {action}ed!'}, status=200)
    except Assignment.DoesNotExist:
        return JsonResponse({'error': 'Assignment not found'}, status=404)
