

from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('my/images/<str:m_id>',views.GetImageViewSet.as_view()),
    path('add-member',views.MemberViewSet.as_view()),


]

