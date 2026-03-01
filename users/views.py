from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    """ViewSet для управления профилями пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """Права для действий пользователей"""

        if self.action == "create":
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]


class PaymentViewSet(ModelViewSet):
    """ViewSet для работы с платежами."""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = (
        "paid_course",
        "paid_lesson",
        "payment_method",
    )

    ordering_fields = (
        "payment_date",
        "amount",
    )
    ordering = ("-payment_date",)
    permission_classes = (IsAuthenticated,)
