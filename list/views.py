from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AllFlowers
from .serializers import FlowerSerializer


class FlowerView(APIView):
    def get(self, request):
        flowers = AllFlowers.objects.all()
        # return Response({"flowers" : flowers})

        serializer = FlowerSerializer(flowers, many=True)
        return Response({"flowers": serializer.data})
