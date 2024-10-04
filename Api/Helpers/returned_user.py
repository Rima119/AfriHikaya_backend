from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from Account.serializers import ReturnedUserSerializer
from rest_framework import status

def get_token(user, res):
    try:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        user_data = ReturnedUserSerializer(user).data

        # Create a response object to set the cookie
        response = JsonResponse({
            'id': user_data['id'],
            'email': user_data['email'],
            'username': user_data['username'],
            'roles': user_data['roles'],
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name'],
            'country': user_data['country'],
            'native_language': user_data['native_language'],
            'hobbies': user_data['hobbies'],
            'profile_pic_url': user_data['profile_pic_url'],
            'access': access_token,
        }, status=res['status'])

        # Set refresh token in a cookie
        response.set_cookie('refresh_token', str(refresh_token), httponly=True, max_age=60 * 60 * 24 * 7,  # 7 days
                            samesite='Lax')  # CSRF protection
        
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)