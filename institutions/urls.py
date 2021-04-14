from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("ContactDetails", api.ContactDetailsViewSet)
router.register("ContactCategory", api.ContactCategoryViewSet)
router.register("Address", api.AddressViewSet)
router.register("InstitutionCategory", api.InstitutionCategoryViewSet)
router.register("Institution", api.InstitutionViewSet)
router.register("Ownership", api.OwnershipViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("ContactDetails/", views.ContactDetailsListView.as_view(), name="institutions_ContactDetails_list"),
    path("ContactDetails/create/", views.ContactDetailsCreateView.as_view(), name="institutions_ContactDetails_create"),
    path("ContactDetails/detail/<int:pk>/", views.ContactDetailsDetailView.as_view(), name="institutions_ContactDetails_detail"),
    path("ContactDetails/update/<int:pk>/", views.ContactDetailsUpdateView.as_view(), name="institutions_ContactDetails_update"),
    path("ContactCategory/", views.ContactCategoryListView.as_view(), name="institutions_ContactCategory_list"),
    path("ContactCategory/create/", views.ContactCategoryCreateView.as_view(), name="institutions_ContactCategory_create"),
    path("ContactCategory/detail/<int:pk>/", views.ContactCategoryDetailView.as_view(), name="institutions_ContactCategory_detail"),
    path("ContactCategory/update/<int:pk>/", views.ContactCategoryUpdateView.as_view(), name="institutions_ContactCategory_update"),
    path("Address/", views.AddressListView.as_view(), name="institutions_Address_list"),
    path("Address/create/", views.AddressCreateView.as_view(), name="institutions_Address_create"),
    path("Address/detail/<int:pk>/", views.AddressDetailView.as_view(), name="institutions_Address_detail"),
    path("Address/update/<int:pk>/", views.AddressUpdateView.as_view(), name="institutions_Address_update"),
    path("InstitutionCategory/", views.InstitutionCategoryListView.as_view(), name="institutions_MemberCategory_list"),
    path("InstitutionCategory/create/", views.InstitutionCategoryCreateView.as_view(), name="institutions_MemberCategory_create"),
    path("InstitutionCategory/detail/<int:pk>/", views.InstitutionCategoryDetailView.as_view(), name="institutions_MemberCategory_detail"),
    path("InstitutionCategory/update/<int:pk>/", views.InstitutionCategoryUpdateView.as_view(), name="institutions_MemberCategory_update"),
    path("Institution/", views.InstitutionListView.as_view(), name="institutions_Member_list"),
    path("Institution/create/", views.InstitutionCreateView.as_view(), name="institutions_Member_create"),
    path("Institution/detail/<int:pk>/", views.InstitutionDetailView.as_view(), name="institutions_Member_detail"),
    path("Institution/update/<int:pk>/", views.InstitutionUpdateView.as_view(), name="institutions_Member_update"),
    path("Ownership/", views.OwnershipListView.as_view(), name="institutions_Ownership_list"),
    path("Ownership/create/", views.OwnershipCreateView.as_view(), name="institutions_Ownership_create"),
    path("Ownership/detail/<int:pk>/", views.OwnershipDetailView.as_view(), name="institutions_Ownership_detail"),
    path("Ownership/update/<int:pk>/", views.OwnershipUpdateView.as_view(), name="institutions_Ownership_update"),
)
