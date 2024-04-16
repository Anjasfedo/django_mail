from django.shortcuts import redirect


# class IsAuthPageMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_template_response(self, request, response):
#         # List of authentication-related URLs
#         auth_urls = ['accounts//login/', 'accounts//logout/', 'accounts//reset-password/',
#                      'accounts//reset-password-done/', 'accounts//reset-password-complete/', 'accounts//reset/']

#         # Check if the current path is an authentication page
#         is_auth_page = any(request.path.startswith(url) for url in auth_urls)

#         # Add is_auth_page context to the response
#         response.context_data["is_auth_page"] = is_auth_page
#         return response


class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if not request.path.startswith('/accounts/logout/') and not request.path.startswith('/accounts/password-change/'):
                if request.path.startswith('/accounts/'):
                    return redirect('dashboard')
        
        response = self.get_response(request)
        return response
