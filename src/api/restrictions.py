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
        service_info, _ = UserServiceRequestInfo.objects.get_or_create(user=request.user, type=service_type)
        if service_info.number_of_requests != 0:
            service_info.number_of_requests -= 1
            service_info.save()
            return True

        return False


def user_paid_for_service(user, service_type):
    return True
