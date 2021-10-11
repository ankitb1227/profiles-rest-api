from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serlializers


class HelloApiView(APIView):
    """Test API views"""
    serlializer_class = serlializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API view functions"""
        an_apiview = ['Uses Http responses as functions (get, post, put, patch, delete)',
                      'Gives more control over application logic'
                      ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Creating hello message with our name"""
        serlializer = self.serlializer_class(data=request.data)

        if serlializer.is_valid():
            name = serlializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serlializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updating the object"""
        return Response({'method': 'patch'})
