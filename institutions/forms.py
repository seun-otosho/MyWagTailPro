from django import forms
from . import models


class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = models.ContactDetail
        fields = [
            "contact_info",
            "type",
        ]


class ContactCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ContactCategory
        fields = [
            "type",
        ]


class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = [
            "state",
            "country",
            "area",
            "street_address",
        ]


class MemberCategoryForm(forms.ModelForm):
    class Meta:
        model = models.MemberCategory
        fields = [
            "category",
        ]


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = [
            "name",
            "date_licensed",
            "date_re_registered",
            "comments",
            "old_name",
            "contacts",
            "category",
            "ownership",
            "address",
        ]


class OwnershipForm(forms.ModelForm):
    class Meta:
        model = models.Ownership
        fields = [
            "type",
        ]
