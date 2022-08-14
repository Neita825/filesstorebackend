from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.views import APIView


class CreateUser(APIView):
    def post(self, request):
        user = User.objects.create(
                    username=request.POST['username'],
                )
        user.set_password(request.POST['password'])
        user.save()

        return JsonResponse("User Create", safe=False, status=status.HTTP_200_OK)