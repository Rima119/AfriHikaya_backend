from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer, CreateCustomUserSerializer, CustomUserSerializer
from django.contrib.auth.hashers import make_password
from Helpers import upload_to_cloudinary, save_account_serializer, returned_user
from .forms import CustomUserCreationForm
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


# Create your views here.

def home(request):
    return Response({'message': 'Welcome to AfriHikaya API'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    view = TokenObtainPairView.as_view(serializer_class = CustomTokenObtainPairSerializer)
    return view(request._request)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh(request):
   view = TokenRefreshView.as_view()
   return view(request._request)


@api_view(['POST'])
def create(request):
    try:
        form = CustomUserCreationForm(request.data, request.FILES)
        #check if email is already in use
        user_email = CustomUser.objects.filter(email=request.data.get('email')).first()
        if user_email:
            return Response({'error': 'This email is already in use. Please choose a different one.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if form.is_valid():
            image = form.cleaned_data['profile_pic']
            public_id = form.cleaned_data['first_name'] + "_" + form.cleaned_data['last_name'] + "_profile_pic"
            
            uploaded_result = upload_to_cloudinary.upload(image, folder='profile_pics', resource_type="image", public_id=public_id)
            form.cleaned_data['profile_pic_url'] = uploaded_result
            
            serializer = CreateCustomUserSerializer(data=form.cleaned_data)
            
            res = save_account_serializer.save_serializer(serializer, 'User created successfully')
            
            if 'error' in res:
                return Response(res['error'], status=res['status'])
            
            user = serializer.instance
            print(user)
            response = returned_user.get_token(user, res)
            # token = user.get_token()
            # refresh = RefreshToken.for_user(user)
            # access_token = str(refresh.access_token)
            # refresh_token = str(refresh)
            # user_data = CreateCustomUserSerializer(user).data

            # Create a response object to set the cookie
            # response = JsonResponse({
            #     'message': res['message'],
            #     'user': user_data,
            #     'access_token': access_token,
            # }, status=res['status'])
            
            # Set refresh token in a cookie
            # response.set_cookie('refresh_token', str(refresh_token), httponly=True, max_age=60 * 60 * 24 * 7,  # 7 days
            #                     samesite='Lax')  # CSRF protection
            
            return response
        
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#TODO: A route to add roles to a user
@api_view(['POST'])
@permission_classes([IsAdminUser])
async def add_roles(request):
    pass


#TODO: A route to remove roles from a user
@api_view(['POST'])
@permission_classes([IsAdminUser])
async def remove_roles(request):
    pass
