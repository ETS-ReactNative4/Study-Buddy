from django.urls import path
from .views import Create, Join

urlpatterns = [
    path('create/', Create.as_view(), name="create"),
    path('join/', Join.as_view(), name='join')
]
