from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse


class HomeViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def main_view(self, request):
        return JsonResponse({'message': 'server on'})
