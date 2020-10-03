from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from .serializer import UserSerializer
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

@api_view(['POST'])
def authentication(request):
    """
    This function takes care of user authentication, which involves both sign up and sign in.
    It expects two required arguments in both cases, that are: username and password.
    Email is required for sign up.
    """

    # reading request data
    payload = request.data

    # expecting required arguments and setting to variable
    try:
        username = payload['username']
        password = payload['password']
    except:
        return Response({"message": "Data not given in the expected format."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)

    # checks if user with username already exixsts
    if user:
        # logs user in and return data
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        # if user doesn't exist for given credentials
        try:
            # ensuring email was given
            email = payload['email']
        except:
            # concluding the login was incorrect
            return Response({"message": "Invalid Credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        # if email was given continue to registration
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
