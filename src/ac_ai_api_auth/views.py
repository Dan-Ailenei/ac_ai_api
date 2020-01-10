from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.authtoken.models import Token


@login_required
def generate_token_view(request):
    # TODO: it looks like DRF is saving the token key without hashing it, should we use something else ?
    token, _ = Token.objects.get_or_create(user=request.user)
    return render(request, 'ac_ai_api_auth/token.html', {'token': token})
