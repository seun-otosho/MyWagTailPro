from django.db import models
from django.urls import reverse


class ContactDetail(models.Model):

    # Relationships
    type = models.ForeignKey("institutions.ContactCategory", to_field='type', on_delete=models.DO_NOTHING)

    # Fields
    contact_info = models.CharField(max_length=64)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("members_ContactDetails_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("members_ContactDetails_update", args=(self.pk,))


class ContactCategory(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.CharField(max_length=16, unique=True, )
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.type)

    def get_absolute_url(self):
        return reverse("members_ContactCategory_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("members_ContactCategory_update", args=(self.pk,))


class Address(models.Model):

    # Fields
    state = models.CharField(max_length=32)
    country = models.CharField(max_length=64)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    area = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    street_address = models.TextField(max_length=128)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("members_Address_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("members_Address_update", args=(self.pk,))


class MemberCategory(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    category = models.CharField(max_length=64, unique=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.category)

    def get_absolute_url(self):
        return reverse("members_MemberCategory_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("members_MemberCategory_update", args=(self.pk,))


class Member(models.Model):

    # Relationships
    contacts = models.ForeignKey(
        "institutions.ContactDetail", on_delete=models.CASCADE, blank=True, null=True, related_name='contact_details'
    )
    category = models.ForeignKey("institutions.MemberCategory", to_field='category', on_delete=models.DO_NOTHING)  #
    ownership = models.ForeignKey("institutions.Ownership", to_field='type', on_delete=models.CASCADE)  #
    address = models.ForeignKey("institutions.Address", on_delete=models.CASCADE, blank=True, null=True, )

    # Fields
    name = models.CharField(max_length=64)
    date_licensed = models.DateField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    date_re_registered = models.DateField()
    comments = models.TextField(max_length=128)
    old_name = models.CharField(max_length=64)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("members_Member_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("members_Member_update", args=(self.pk,))


class Ownership(models.Model):

    # Fields
    type = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.type)

    def get_absolute_url(self):
        return reverse("members_Ownership_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("members_Ownership_update", args=(self.pk,))
