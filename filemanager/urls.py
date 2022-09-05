from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from filemanager.views import BrowserView, DetailView, UploadView, UploadFileView, DirectoryCreateView

app_name = 'namespace'
urlpatterns = (
    path('', BrowserView.as_view(), name='browser'),
    path('detail/', DetailView.as_view(), name='detail'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('upload/file/', csrf_exempt(UploadFileView.as_view()), name='upload-file'),
    path('create/directory/', DirectoryCreateView.as_view(), name='create-directory'),
)
