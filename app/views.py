from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response 

from . import serializers
from rest_framework import status
# Create your views here.

class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview=[
            "Uses HTTP methods as function  (get, post, patch, put, delete)",
            "It is similar to a traditional Django View",
            "Gives you the most control over the logic",
            "Is mapped manually tp urls"
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})


    def post(self, request):
        """Create Hello Message with a Name"""

        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)

            return Response({"message": message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""

        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({"method": "delete"})


class HelloViewSet(viewsets.ViewSet):
    """Tests Api View"""

    def list(self, request):
        """Return a Hello Message"""

        a_viewset=[
            "Uses actions (list, create, retrieve, update, partial_update)"
            "Automatically maps to URLs using Routers"
            "Provides more functionality with less code"
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})
