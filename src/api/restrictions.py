from django.db.models import F, Q
from rest_framework import permissions
from rest_framework import throttling
from api.models import UserServiceRequestInfo


class PaidForServiceOrHasRequestsLeft(permissions.BasePermission):
    """
    Custom permission to only allow the users that paid
    for the service or have leftover requests to make
    requests
    """

    def has_permission(self, request, view):
        service_type = view.service_type
        service_info, _ = UserServiceRequestInfo.objects.get_or_create(user=request.user, type=service_type)
        return service_info.number_of_requests or user_paid_for_service(request.user, service_type)


class LimitedRequestsThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        service_type = view.service_type

        UserServiceRequestInfo.objects.get_or_create(user=request.user, type=service_type)
        updated = UserServiceRequestInfo.objects \
            .filter(user=request.user, type=service_type, number_of_requests__gt=0) \
            .update(number_of_requests=F('number_of_requests') - 1)

        return updated == 1


def user_paid_for_service(user, service_type):
    return True
