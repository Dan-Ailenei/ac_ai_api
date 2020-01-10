from django.db import models
from ac_ai_api_auth.models import AcAiApiUser


# be aware that this is not a db model
class Result:
    def __init__(self, result):
        self.result = result


class UserServiceRequestInfo(models.Model):
    NLP = 0
    SERVICE_TYPE_CHOICES = ((NLP, 'nlp'),)

    number_of_requests = models.IntegerField(default=0)
    user = models.ForeignKey(AcAiApiUser, on_delete=models.CASCADE, related_name='service_info')
    type = models.IntegerField(choices=SERVICE_TYPE_CHOICES)

    class Meta:
        unique_together = ['type', 'user']
