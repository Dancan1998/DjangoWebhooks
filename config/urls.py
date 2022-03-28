from django.contrib import admin
from django.urls import path
from hook.views import home, api_git_msg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home-view'),
    path('github/', api_git_msg, name='api-github'),
]