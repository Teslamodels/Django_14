from django.urls import path
from .views import A

urlpatterns = [
    path('', A.as_view(), name='a'),
]