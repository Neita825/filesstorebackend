from . import upload, download, filesList
from django.urls import path, re_path

app_name = "storage"

urlpatterns = [
    path("upload/", upload.UploadFile.as_view(), name="uploadFile"),
    path("filesList/", filesList.FilesList.as_view(), name="filesList"),
    re_path(r'.*', download.DownloadFile.as_view(), name="downloadFile"),
]


