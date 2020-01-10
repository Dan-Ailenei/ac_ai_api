from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class AcAiApiUser(AbstractUser):
    number_of_requests = models.IntegerField(default=0)

    def paid_for_service(self, service_name):
        # TODO: determine if the user paid for the service or not
        return False
