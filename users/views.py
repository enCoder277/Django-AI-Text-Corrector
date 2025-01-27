from django.contrib.auth.views import LoginView

from .forms import LoginUserForm


class LoginUser(LoginView):
    redirect_authenticated_user = True
    form_class = LoginUserForm
    template_name = 'users/login.html'
