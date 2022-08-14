from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import response, status
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token

from .models import File
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase


class FilesTestCase(APITestCase):
    def setUp(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        file_test = SimpleUploadedFile("file_test.jpg", b"File for test")
        file_test.name = 'file_test.jpg'
        File.objects.create(
                url="url1",
                uploadedFile=file_test,
                user=user1.id,
                fileName=file_test.name,
                revision=0,
        )
        File.objects.create(
                url="url1",
                uploadedFile=file_test,
                user=user1.id,
                fileName=file_test.name,
                revision=1,
        )
        File.objects.create(
                url="url2",
                uploadedFile=file_test,
                user=user1.id,
                fileName=file_test.name,
                revision=0,
        )
        File.objects.create(
                url="url1",
                uploadedFile=file_test,
                user=user2.id,
                fileName=file_test.name,
                revision=0,
        )
        File.objects.create(
                url="url3",
                uploadedFile=file_test,
                user=user2.id,
                fileName=file_test.name,
                revision=0,
        )

    def testUser1(self):
        user = User.objects.get(username='user1')
        self.client.force_authenticate(user=user)
        response = self.client.get('/filesList/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'url': 'url1', 'lastRevision': 1}, {'url': 'url2', 'lastRevision': 0}]
        )
    def testUser2(self):
        user = User.objects.get(username='user2')
        self.client.force_authenticate(user=user)
        response = self.client.get('/filesList/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'url': 'url1', 'lastRevision': 0}, {'url': 'url3', 'lastRevision': 0}]
        )
    def testUploadFile(self):
        user = User.objects.get(username='user1')
        self.client.force_authenticate(user=user)
        file_test = SimpleUploadedFile("file_test.jpg", b"File for test")
        self.client.post('/upload/', {'url': "url3", 'file': file_test})
        response = self.client.get('/filesList/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'url': 'url1', 'lastRevision': 1}, {'url': 'url2', 'lastRevision': 0}, {'url': 'url3', 'lastRevision': 0}]
        )
    def testUploadFileWithRevision(self):
        user = User.objects.get(username='user1')
        self.client.force_authenticate(user=user)
        file_test = SimpleUploadedFile("file_test.jpg", b"File for test")
        self.client.post('/upload/', {'url': "url1", 'file': file_test})
        response = self.client.get('/filesList/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'url': 'url1', 'lastRevision': 2}, {'url': 'url2', 'lastRevision': 0}]
        )
    def testDownload(self):
        user = User.objects.get(username='user1')
        self.client.force_authenticate(user=user)
        response = self.client.get('/url1?revision=0', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'File for test')