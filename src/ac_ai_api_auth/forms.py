from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class TokenForm(forms.Form):
    def __init__(self, *args, user, token_limit_per_user, **kwargs):
        super().__init__(*args, **kwargs)
        self.token_limit_per_user = token_limit_per_user
        self.user = user

    def clean(self):
        super().clean()
        if self.token_limit_per_user is not None:
            now = timezone.now()
            token = self.user.auth_token_set.filter(expiry__gt=now)
            if token.count() >= self.token_limit_per_user:
                raise ValidationError('Maximum amount of tokens allowed per user exceeded.')
