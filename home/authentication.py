from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User

class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Retrieve the username and password from the request
        username = request.data.get('username')
        password = request.data.get('password')

        # Perform authentication logic
        try:
            user = User.objects.get(user_name=username)
            if user.password == password:
                return (user, None)
            else:
                raise AuthenticationFailed('Invalid password')
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')
