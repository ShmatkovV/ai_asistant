from apps.users.models import User
from rest_framework import  serializers

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
		read_only_fields = ('id',)
	
	