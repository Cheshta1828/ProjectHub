import json
import requests
from jose.backends.cryptography_backend import CryptographyBackend
from jose.constants import ALGORITHMS
from jose.exceptions import JWTError
from jose.utils import base64url_decode
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from django.conf import settings

CLIENT_ID = ''
CLIENT_SECRET = ''
AUTH0_DOMAIN = ''

# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = BaseUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        auth0_data = {
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'connection': 'Username-Password-Authentication',  # Replace with your Auth0 connection name
                'email': request.data['email'],
                'password': request.data['password'],
                # Add any additional user metadata here
             }
        response = requests.post(f'https://{AUTH0_DOMAIN}/dbconnections/signup', json=auth0_data)

        if response.status_code == 200:
                # User successfully registered with Auth0
                return Response({'message': 'User registered successfully'})

        return Response({'error': 'Failed to register user with Auth0'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        