from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ContactDetailsViewSet(viewsets.ModelViewSet):
    """ViewSet for the ContactDetails class"""

    queryset = models.ContactDetail.objects.all()
    serializer_class = serializers.ContactDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the ContactCategory class"""

    queryset = models.ContactCategory.objects.all()
    serializer_class = serializers.ContactCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressViewSet(viewsets.ModelViewSet):
    """ViewSet for the Address class"""

    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the MemberCategory class"""

    queryset = models.MemberCategory.objects.all()
    serializer_class = serializers.MemberCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberViewSet(viewsets.ModelViewSet):
    """ViewSet for the Member class"""

    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class OwnershipViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ownership class"""

    queryset = models.Ownership.objects.all()
    serializer_class = serializers.OwnershipSerializer
    permission_classes = [permissions.IsAuthenticated]
