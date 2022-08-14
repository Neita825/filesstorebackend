from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return JsonResponse({'auth': False}, safe=False, status=status.HTTP_200_OK)


class Session(APIView):
    def get(self, request):
        if request.user:
            return JsonResponse({'auth': request.user.username}, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'auth': False}, safe=False, status=status.HTTP_200_OK)


