from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from account.models import Account 
import jwt

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("jwt-auth")

        if not token:
            return None

        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded.get("id")

            if not user_id:
                raise AuthenticationFailed("Invalid Token")

            account = Account.objects.get(id=user_id)
            return (account, None)
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.DecodeError:
            raise AuthenticationFailed("Error decoding token")
        except Account.DoesNotExist:
            raise AuthenticationFailed("User not found")