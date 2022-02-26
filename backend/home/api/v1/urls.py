from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ArticlesViewSet,
    EvenementsViewSet,
    ListecategorieViewSet,
    ListeroleViewSet,
    RencontresViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("listecategorie", ListecategorieViewSet)
router.register("listerole", ListeroleViewSet)
router.register("articles", ArticlesViewSet)
router.register("evenements", EvenementsViewSet)
router.register("rencontres", RencontresViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
