from rest_framework import viewsets
from home.models import Articles, Evenements, Listecategorie, Listerole, Rencontres
from .serializers import (
    ArticlesSerializer,
    EvenementsSerializer,
    ListecategorieSerializer,
    ListeroleSerializer,
    RencontresSerializer,
)
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class ListecategorieViewSet(viewsets.ModelViewSet):
    serializer_class = ListecategorieSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Listecategorie.objects.all()


class ListeroleViewSet(viewsets.ModelViewSet):
    serializer_class = ListeroleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Listerole.objects.all()


class ArticlesViewSet(viewsets.ModelViewSet):
    serializer_class = ArticlesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Articles.objects.all()


class EvenementsViewSet(viewsets.ModelViewSet):
    serializer_class = EvenementsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Evenements.objects.all()


class RencontresViewSet(viewsets.ModelViewSet):
    serializer_class = RencontresSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Rencontres.objects.all()
