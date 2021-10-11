from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API views"""

    def get(self, request, format=None):
        """Returns a list of API view functions"""
        an_apiview = ['Uses Http responses as functions (get, post, put, patch, delete)']

        return Response({'message': 'hello!', 'an_apiview': an_apiview})