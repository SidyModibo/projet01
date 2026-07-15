from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from django.conf import settings

class CookieJWTAuthentication(JWTAuthentication):
    """
    Custom JWTAuthentication qui lit le token depuis un cookie HttpOnly
    """
    def authenticate(self, request):
        # Essayer de récupérer le token depuis le cookie
        access_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
        
        if access_token:
            try:
                validated_token = self.get_validated_token(access_token)
                return self.get_user(validated_token), validated_token
            except InvalidToken:
                raise AuthenticationFailed('Token invalide ou expiré')
        
        # Fallback sur le header Authorization
        return super().authenticate(request)