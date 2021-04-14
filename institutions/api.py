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


class InstitutionCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the InstitutionCategory class"""

    queryset = models.InstitutionCategory.objects.all()
    serializer_class = serializers.InstitutionCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class InstitutionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Institution class"""

    queryset = models.Institution.objects.all()
    serializer_class = serializers.InstitutionSerializer
    permission_classes = [permissions.IsAuthenticated]


class OwnershipViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ownership class"""

    queryset = models.Ownership.objects.all()
    serializer_class = serializers.OwnershipSerializer
    permission_classes = [permissions.IsAuthenticated]
