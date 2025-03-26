from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from apps.users.serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		user = serializer.save(is_active=True)
		token, created = Token.objects.get_or_create(user=user)
		return Response({
			'user': serializer.data,
			'token': token.key
		}, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
	username = request.data.get('username')
	password = request.data.get('password')
	user = authenticate(username=username, password=password)
	
	if user:
		token, created = Token.objects.get_or_create(user=user)
		serializer = UserSerializer(user)
		
		return Response({
			'user': serializer.data,
			'token': token.key
		}, status=status.HTTP_200_OK)
	
	return Response(
		{'error': 'Invalid credentials'},
		status=status.HTTP_401_UNAUTHORIZED
	)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
	request.user.auth_token.delete()
	new_token = Token.objects.create(user=request.user)
	
	return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
