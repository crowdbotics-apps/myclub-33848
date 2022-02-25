from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ListecategorieViewSet, ListeroleViewSet, UtilisateursViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("utilisateurs", UtilisateursViewSet)
router.register("listecategorie", ListecategorieViewSet)
router.register("listerole", ListeroleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
