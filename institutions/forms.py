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


class InstitutionCategoryForm(forms.ModelForm):
    class Meta:
        model = models.InstitutionCategory
        fields = [
            "category",
        ]


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = models.Institution
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
