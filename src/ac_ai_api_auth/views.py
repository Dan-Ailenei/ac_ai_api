from django.contrib.auth import login, user_logged_in
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from knox.models import AuthToken
from rest_framework import permissions
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from ac_ai_api_auth.forms import TokenForm


@login_required
def generate_token_view(request):
    api_login_view = ApiLoginView()
    token_limit_per_user = api_login_view.get_token_limit_per_user()
    token, expiry_date = None, None

    if request.method == 'POST':
        form = TokenForm(request.POST, user=request.user, token_limit_per_user=token_limit_per_user)
        if form.is_valid():
            instance, token = AuthToken.objects.create(request.user)
            expiry_date = instance.expiry
    else:
        form = TokenForm(user=request.user, token_limit_per_user=token_limit_per_user)

    return render(request, 'ac_ai_api_auth/token.html', {'form': form, 'token': token, 'expiry_date': expiry_date})


class ApiLoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)
