from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.functional import SimpleLazyObject

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            def get_user():
                try:
                    user_auth_tuple = JWTAuthentication().authenticate(request)
                    if user_auth_tuple is not None:
                        user, token = user_auth_tuple
                        return user
                except Exception:
                    pass
                return request.user

            request.user = SimpleLazyObject(get_user)
        return self.get_response(request)
