from django.http import Http404
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from api.algorithms.nlp import compute_result
from api.models import Result, UserServiceRequestInfo
from api.restrictions import PaidForServiceOrHasRequestsLeft, LimitedRequestsThrottle, user_paid_for_service
from api.serializers import ResultSerializer


class ApiUserRateThrottle(UserRateThrottle):
    rate = '1000/month'


class RestrictedApiMixin:
    permission_classes = [IsAuthenticated, PaidForServiceOrHasRequestsLeft]
    authentication_classes = [TokenAuthentication]
    user_rate_throttle_classes = [ApiUserRateThrottle]

    def get_throttles(self):
        if user_paid_for_service(self.request.user, self.service_type):
            return self.get_user_rate_throttles()
        return [LimitedRequestsThrottle()]

    def get_user_rate_throttles(self):
        return [user_rate_throttle() for user_rate_throttle in self.user_rate_throttle_classes]


class NlpResultView(RestrictedApiMixin, APIView):
    service_type = UserServiceRequestInfo.NLP

    def get_result(self):
        try:
            return Result(compute_result())
        # TODO: decide if algorithm can throw an exception
        except Exception as ex:
            raise Http404

    def get(self, request):
        result = self.get_result()
        serializer = ResultSerializer(result)
        return Response(serializer.data)
