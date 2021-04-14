from rest_framework import serializers

from . import models
from .models import MemberCategory, Ownership, Member


class ContactDetailsSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(queryset=models.ContactCategory.objects.all(), slug_field='type')

    class Meta:
        model = models.ContactDetail
        fields = [
            "contact_info",
            "last_updated",
            "created",
            #
            'type',
        ]


class ContactCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactCategory
        fields = [
            "last_updated",
            "type",
            "created",
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = [
            "state",
            "country",
            "last_updated",
            "area",
            "created",
            "street_address",
        ]


class MemberCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MemberCategory
        fields = [
            "created",
            "category",
            "last_updated",
        ]


class MemberSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=models.MemberCategory.objects.all(), slug_field='category')
    ownership = serializers.SlugRelatedField(queryset=models.Ownership.objects.all(), slug_field='type')

    contacts = ContactDetailsSerializer(many=True,  )

    class Meta:
        model = models.Member
        fields = [
            "name",
            "date_licensed",
            "created",
            "last_updated",
            "date_re_registered",
            "comments",
            "old_name",
            # 
            'category',
            'ownership',
            #
            'contacts',
        ]
        depth = 1

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        member = models.Member.objects.create(**validated_data)
        for contact_detail in contacts_data:
            models.ContactDetail.objects.create(member=member, **contact_detail)
        return member

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts')
        # member = models.Member.objects.update_or_create(default={"id": instance.id}, **validated_data)
        for contact_detail in contacts_data:
            models.ContactDetail.objects.update_or_create(member=instance, **contact_detail)
        return instance

    # @staticmethod
    # def setup_eager_loading(queryset):
    #     queryset = queryset.select_related('contacts', )
    #     return queryset


class OwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ownership
        fields = [
            "type",
            "created",
            "last_updated",
        ]
