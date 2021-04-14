from django.contrib import admin
from django import forms

from . import models


class ContactDetailsAdminForm(forms.ModelForm):

    class Meta:
        model = models.ContactDetail
        fields = "__all__"


class ContactDetailsAdmin(admin.ModelAdmin):
    form = ContactDetailsAdminForm
    list_display = [
        "contact_info",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "contact_info",
        "last_updated",
        "created",
    ]


class ContactCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.ContactCategory
        fields = "__all__"


class ContactCategoryAdmin(admin.ModelAdmin):
    form = ContactCategoryAdminForm
    list_display = [
        "last_updated",
        "type",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "type",
        "created",
    ]


class AddressAdminForm(forms.ModelForm):

    class Meta:
        model = models.Address
        fields = "__all__"


class AddressAdmin(admin.ModelAdmin):
    form = AddressAdminForm
    list_display = [
        "state",
        "country",
        "last_updated",
        "area",
        "created",
        "street_address",
    ]
    readonly_fields = [
        "state",
        "country",
        "last_updated",
        "area",
        "created",
        "street_address",
    ]


class MemberCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.MemberCategory
        fields = "__all__"


class MemberCategoryAdmin(admin.ModelAdmin):
    form = MemberCategoryAdminForm
    list_display = [
        "created",
        "category",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "category",
        "last_updated",
    ]


class MemberAdminForm(forms.ModelForm):

    class Meta:
        model = models.Member
        fields = "__all__"


class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm
    list_display = [
        "name",
        "date_licensed",
        "created",
        "last_updated",
        "date_re_registered",
        "comments",
        "old_name",
    ]
    readonly_fields = [
        "name",
        "date_licensed",
        "created",
        "last_updated",
        "date_re_registered",
        "comments",
        "old_name",
    ]


class OwnershipAdminForm(forms.ModelForm):

    class Meta:
        model = models.Ownership
        fields = "__all__"


class OwnershipAdmin(admin.ModelAdmin):
    form = OwnershipAdminForm
    list_display = [
        "type",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "type",
        "created",
        "last_updated",
    ]


admin.site.register(models.ContactDetail, ContactDetailsAdmin)
admin.site.register(models.ContactCategory, ContactCategoryAdmin)
admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.MemberCategory, MemberCategoryAdmin)
admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.Ownership, OwnershipAdmin)
