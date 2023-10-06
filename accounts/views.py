# import json
# import requests
# from jose.backends.cryptography_backend import CryptographyBackend
# from jose.constants import ALGORITHMS
# from jose.exceptions import JWTError
# from jose.utils import base64url_decode
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from django.conf import settings
import os
import uuid
from io import BytesIO  #basic input/output operation
from PIL import Image #Imported to compress images
from django.core.files import File
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout

CLIENT_ID = ''
CLIENT_SECRET = ''
AUTH0_DOMAIN = ''
@api_view(['POST'])
def register(request):
    print("this is the data " , request.data)
    serializer = BaseUserSerializer(data=request.data)
    if serializer.is_valid():
        validated_data=serializer.validated_data
        profile_pic = request.data['profile_pic']
        filename, ext = os.path.splitext(profile_pic.name)
        im = Image.open(profile_pic)
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im_io = BytesIO() 
        im.save(im_io, 'JPEG', quality=60) 
        new_image = File(im_io, name=f"{request.data['email']}_profile_pic_{uuid.uuid4().hex}.jpeg")
        request.data['profile_pic'] = new_image
        print("this is the request data " , request.data)
        BU = BaseUser.objects.create(email=validated_data['email'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],profile_pic=request.data['profile_pic'],acc_type=validated_data['acc_type'],auth0_id=validated_data['auth0_id'])
        BU.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        print("this is the error " , serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        