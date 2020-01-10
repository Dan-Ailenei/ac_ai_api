from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from ac_ai_api_auth.permisions import PaidForServiceOrHasRequestsLeft
from nlp.algorithms.nlp import compute_result
from nlp.models import Result
from nlp.serializers import ResultSerializer


class NlpResultView(APIView):
    permission_classes = [IsAuthenticated, PaidForServiceOrHasRequestsLeft]
    service_name = 'nlp'

    def get_throttles(self):
        return [UserRateThrottle()]

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
