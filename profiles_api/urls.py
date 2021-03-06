from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()

router.register("hello_viewset", views.HelloViewSet, basename="hello")
router.register("profile", viewset=views.UserProfileViewSet)
router.register("feed", viewset=views.UserProfileFeedViewSet)

urlpatterns = [
    path("hello_apiview/", views.HelloApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
