from rest_framework import permissions


class PaidForServiceOrHasRequestsLeft(permissions.BasePermission):
    """
    Custom permission to only allow the users that paid
    for the service or have leftover requests to make
    requests
    """

    def has_permission(self, request, view):
        user = request.user
        return user.number_of_requests or user.paid_for_service(view.service_name)
