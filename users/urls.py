from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register("users", UserViewSet)  # /users/users/
router.register("payments", PaymentViewSet)  # /users/payments/

urlpatterns = [
    path("", include(router.urls)),
    path(
        "login/",TokenObtainPairView.as_view(),name="login/"),
    path(
        "token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
]
