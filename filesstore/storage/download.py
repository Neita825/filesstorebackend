import logging

from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from . import models


class DownloadFile(APIView):
    def get(self, request):
        revision = request.GET.get('revision', None)
        if revision == None:
            file = models.File.objects.filter(url=request.path.strip("/"), user=request.user.id).order_by('revision').last()
        else:
            file = models.File.objects.get(url=request.path.strip("/"), user=request.user.id, revision=revision)
        filename = file.fileName
        headers = {'Access-Control-Expose-Headers': 'Content-Disposition, filename'}
        response = HttpResponse(file.uploadedFile, content_type='application/force-download', headers=headers)
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        response['filename'] = filename

        return response
