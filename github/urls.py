

from django.urls import path
from .views import GitHubView, SisterView

urlpatterns = [
    path('', GitHubView.as_view(), name='github-home'),
    path('sister/, SisterView.as_view(), name='sister-page')
]
