class IsAuthPageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        # List of authentication-related URLs
        auth_urls = ['/reset-password/',
                     '/reset-password-done/', '/reset-password-complete/', '/reset/']

        # Check if the current path is an authentication page
        is_auth_page = any(request.path.startswith(url) for url in auth_urls)

        # Add is_auth_page context to the response
        response.context_data["is_auth_page"] = is_auth_page
        return response
