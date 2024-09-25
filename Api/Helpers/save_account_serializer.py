from rest_framework import status
from django.contrib.auth.hashers import make_password

def save_serializer(serializer, succ_message):
    try:
        if serializer.is_valid():
            if serializer.validated_data['roles'] is None or serializer.validated_data['roles'] == '':
                serializer.validated_data['roles'] = 'User'
            password = serializer.validated_data['password']
            harshed_password = make_password(password)
            serializer.validated_data['password'] = harshed_password
            serializer.save()
            return {'message': succ_message, 'status': status.HTTP_201_CREATED}
        return {'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        return {'error': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}