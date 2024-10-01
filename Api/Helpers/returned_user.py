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
            'message': res['message'],
            'user': user_data,
            'access_token': access_token,
        }, status=res['status'])

        # Set refresh token in a cookie
        response.set_cookie('refresh_token', str(refresh_token), httponly=True, max_age=60 * 60 * 24 * 7,  # 7 days
                            samesite='Lax')  # CSRF protection
        
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)