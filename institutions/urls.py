from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("ContactDetails", api.ContactDetailsViewSet)
router.register("ContactCategory", api.ContactCategoryViewSet)
router.register("Address", api.AddressViewSet)
router.register("MemberCategory", api.MemberCategoryViewSet)
router.register("Member", api.MemberViewSet)
router.register("Ownership", api.OwnershipViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("members/ContactDetails/", views.ContactDetailsListView.as_view(), name="members_ContactDetails_list"),
    path("members/ContactDetails/create/", views.ContactDetailsCreateView.as_view(), name="members_ContactDetails_create"),
    path("members/ContactDetails/detail/<int:pk>/", views.ContactDetailsDetailView.as_view(), name="members_ContactDetails_detail"),
    path("members/ContactDetails/update/<int:pk>/", views.ContactDetailsUpdateView.as_view(), name="members_ContactDetails_update"),
    path("members/ContactCategory/", views.ContactCategoryListView.as_view(), name="members_ContactCategory_list"),
    path("members/ContactCategory/create/", views.ContactCategoryCreateView.as_view(), name="members_ContactCategory_create"),
    path("members/ContactCategory/detail/<int:pk>/", views.ContactCategoryDetailView.as_view(), name="members_ContactCategory_detail"),
    path("members/ContactCategory/update/<int:pk>/", views.ContactCategoryUpdateView.as_view(), name="members_ContactCategory_update"),
    path("members/Address/", views.AddressListView.as_view(), name="members_Address_list"),
    path("members/Address/create/", views.AddressCreateView.as_view(), name="members_Address_create"),
    path("members/Address/detail/<int:pk>/", views.AddressDetailView.as_view(), name="members_Address_detail"),
    path("members/Address/update/<int:pk>/", views.AddressUpdateView.as_view(), name="members_Address_update"),
    path("members/MemberCategory/", views.MemberCategoryListView.as_view(), name="members_MemberCategory_list"),
    path("members/MemberCategory/create/", views.MemberCategoryCreateView.as_view(), name="members_MemberCategory_create"),
    path("members/MemberCategory/detail/<int:pk>/", views.MemberCategoryDetailView.as_view(), name="members_MemberCategory_detail"),
    path("members/MemberCategory/update/<int:pk>/", views.MemberCategoryUpdateView.as_view(), name="members_MemberCategory_update"),
    path("members/Member/", views.MemberListView.as_view(), name="members_Member_list"),
    path("members/Member/create/", views.MemberCreateView.as_view(), name="members_Member_create"),
    path("members/Member/detail/<int:pk>/", views.MemberDetailView.as_view(), name="members_Member_detail"),
    path("members/Member/update/<int:pk>/", views.MemberUpdateView.as_view(), name="members_Member_update"),
    path("members/Ownership/", views.OwnershipListView.as_view(), name="members_Ownership_list"),
    path("members/Ownership/create/", views.OwnershipCreateView.as_view(), name="members_Ownership_create"),
    path("members/Ownership/detail/<int:pk>/", views.OwnershipDetailView.as_view(), name="members_Ownership_detail"),
    path("members/Ownership/update/<int:pk>/", views.OwnershipUpdateView.as_view(), name="members_Ownership_update"),
)
