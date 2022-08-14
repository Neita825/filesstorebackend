from django.db.models import Max
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from . import models

class FilesList(APIView):
    def get(self, request):
        files = models.File.objects\
            .filter(user=request.user.id)\
            .values('url')\
            .annotate(lastRevision=Max('revision'))
        filesThisUser = []
        for element in files:
                filesThisUser.append(element)
        return JsonResponse(filesThisUser, safe=False, status=status.HTTP_200_OK)