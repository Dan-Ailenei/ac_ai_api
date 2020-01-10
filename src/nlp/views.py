from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from nlp.algorithms.nlp import compute_result
from nlp.models import Result
from nlp.serializers import ResultSerializer


def index(request):
    return render(request, 'nlp/index.html', {})


class NlpResultView(APIView):
    permission_classes = [permissions.IsAuthenticated]

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
