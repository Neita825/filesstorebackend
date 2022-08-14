from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from . import models


class UploadFile(APIView):
    def post(self, request):
        if request.method == "POST":
            url = request.POST["url"]
            uploadedFile = request.FILES["file"]
            user = request.user.id
            newRevision = 0
            lastRevision = models.File.objects.filter(url=url, user=user).order_by('revision').last()
            if lastRevision:
                newRevision = lastRevision.revision + 1
            file = models.File(
                url=url,
                uploadedFile=uploadedFile,
                user=user,
                fileName=uploadedFile,
                revision=newRevision,
            )
            file.save()
        return JsonResponse({'upload': request.user.id}, safe=False, status=status.HTTP_200_OK)