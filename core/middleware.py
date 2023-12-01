# core/middleware.py

from django.http import HttpResponseForbidden

class RestrictedAccessMiddleware:
    UNREGISTERED_DENIED_URLS = [
        '/Reparaciones',
        '/Vista%20tecnico',
        '/adminlogin/',
        '/admin',
    ]

    REGISTERED_DENIED_URLS = [
        '/adminlogin/',
        '/admin',
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            # User is not authenticated (unregistered user)
            if request.path in self.UNREGISTERED_DENIED_URLS:
                return HttpResponseForbidden("Permission Denied")

        elif request.user.is_authenticated:
            # User is authenticated (registered user)
            if request.path in self.REGISTERED_DENIED_URLS:
                return HttpResponseForbidden("Permission Denied")

        return self.get_response(request)
