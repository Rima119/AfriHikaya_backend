from rest_framework import status

def sync_save_serializer(serializer, succ_message):
    if serializer.is_valid():
        serializer.save()
        return {'message': succ_message, 'status': status.HTTP_201_CREATED}
    return {'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST}
