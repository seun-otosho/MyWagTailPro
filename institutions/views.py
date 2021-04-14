from django.views import generic
from . import models
from . import forms


class ContactDetailsListView(generic.ListView):
    model = models.ContactDetail
    form_class = forms.ContactDetailForm


class ContactDetailsCreateView(generic.CreateView):
    model = models.ContactDetail
    form_class = forms.ContactDetailForm


class ContactDetailsDetailView(generic.DetailView):
    model = models.ContactDetail
    form_class = forms.ContactDetailForm


class ContactDetailsUpdateView(generic.UpdateView):
    model = models.ContactDetail
    form_class = forms.ContactDetailForm
    pk_url_kwarg = "pk"


class ContactCategoryListView(generic.ListView):
    model = models.ContactCategory
    form_class = forms.ContactCategoryForm


class ContactCategoryCreateView(generic.CreateView):
    model = models.ContactCategory
    form_class = forms.ContactCategoryForm


class ContactCategoryDetailView(generic.DetailView):
    model = models.ContactCategory
    form_class = forms.ContactCategoryForm


class ContactCategoryUpdateView(generic.UpdateView):
    model = models.ContactCategory
    form_class = forms.ContactCategoryForm
    pk_url_kwarg = "pk"


class AddressListView(generic.ListView):
    model = models.Address
    form_class = forms.AddressForm


class AddressCreateView(generic.CreateView):
    model = models.Address
    form_class = forms.AddressForm


class AddressDetailView(generic.DetailView):
    model = models.Address
    form_class = forms.AddressForm


class AddressUpdateView(generic.UpdateView):
    model = models.Address
    form_class = forms.AddressForm
    pk_url_kwarg = "pk"


class MemberCategoryListView(generic.ListView):
    model = models.MemberCategory
    form_class = forms.MemberCategoryForm


class MemberCategoryCreateView(generic.CreateView):
    model = models.MemberCategory
    form_class = forms.MemberCategoryForm


class MemberCategoryDetailView(generic.DetailView):
    model = models.MemberCategory
    form_class = forms.MemberCategoryForm


class MemberCategoryUpdateView(generic.UpdateView):
    model = models.MemberCategory
    form_class = forms.MemberCategoryForm
    pk_url_kwarg = "pk"


class MemberListView(generic.ListView):
    model = models.Member
    form_class = forms.MemberForm


class MemberCreateView(generic.CreateView):
    model = models.Member
    form_class = forms.MemberForm


class MemberDetailView(generic.DetailView):
    model = models.Member
    form_class = forms.MemberForm


class MemberUpdateView(generic.UpdateView):
    model = models.Member
    form_class = forms.MemberForm
    pk_url_kwarg = "pk"


class OwnershipListView(generic.ListView):
    model = models.Ownership
    form_class = forms.OwnershipForm


class OwnershipCreateView(generic.CreateView):
    model = models.Ownership
    form_class = forms.OwnershipForm


class OwnershipDetailView(generic.DetailView):
    model = models.Ownership
    form_class = forms.OwnershipForm


class OwnershipUpdateView(generic.UpdateView):
    model = models.Ownership
    form_class = forms.OwnershipForm
    pk_url_kwarg = "pk"
