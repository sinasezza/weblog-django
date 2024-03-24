from django.shortcuts import redirect
from django.contrib import messages

class LogoutRequiredMixin:
    """Verify that the current user is not authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, "You should log out to see this page.")
            return redirect('home') 
        return super().dispatch(request, *args, **kwargs)
