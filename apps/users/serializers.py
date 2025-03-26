from apps.users.models import User
from rest_framework import  serializers

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
		read_only_fields = ('id',)
	
	def create(self, validated_data):
		user = User.objects.create_user(
			username=validated_data['username'],
			password=validated_data['password'],
		)
		return user