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


class InstitutionCategoryListView(generic.ListView):
    model = models.InstitutionCategory
    form_class = forms.InstitutionCategoryForm


class InstitutionCategoryCreateView(generic.CreateView):
    model = models.InstitutionCategory
    form_class = forms.InstitutionCategoryForm


class InstitutionCategoryDetailView(generic.DetailView):
    model = models.InstitutionCategory
    form_class = forms.InstitutionCategoryForm


class InstitutionCategoryUpdateView(generic.UpdateView):
    model = models.InstitutionCategory
    form_class = forms.InstitutionCategoryForm
    pk_url_kwarg = "pk"


class InstitutionListView(generic.ListView):
    model = models.Institution
    form_class = forms.InstitutionForm


class InstitutionCreateView(generic.CreateView):
    model = models.Institution
    form_class = forms.InstitutionForm


class InstitutionDetailView(generic.DetailView):
    model = models.Institution
    form_class = forms.InstitutionForm


class InstitutionUpdateView(generic.UpdateView):
    model = models.Institution
    form_class = forms.InstitutionForm
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
