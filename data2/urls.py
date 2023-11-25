from django.urls import path
from .views import B

urlpatterns = [
    path('', B.as_view(), name='b'),
]