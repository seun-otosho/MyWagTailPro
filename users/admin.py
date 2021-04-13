# Register your models here.
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.db.models import Q

from .forms import UserChangeForm, UserCreationForm
from .models import MyUser


class MemberFilter(SimpleListFilter):
    # states_kv = states()
    # states_vk = {v: k for k, v in states().items()}
    title = 'Member'  # or use _('state') for translated title
    parameter_name = 'member'

    def lookups(self, request, model_admin):
        member_lu = set([o.member for o in model_admin.model.objects.all()]) if request.user.is_admin else set(
            [o.member for o in model_admin.model.objects.filter(
                member=request.user.member)]
        )
        return [(s, s) for s in member_lu if s not in [None]]
        # + [(c, v) for c, v in self.states_kv.items()]

    def queryset(self, request, queryset):
        value = self.value()

        if value:
            # c_val = value.lower().replace('state', '').strip() if 'state' in value.lower() else value
            # c_val = c_val.title()
            return queryset.filter(
                Q(member__iexact=value)
                # | Q(state=self.states_vk.get(c_val, value))
            )


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # 'date_of_birth',
    list_display = ('email', 'is_active', 'is_admin', 'is_staff', ) # 'member', 
    list_filter = ('is_admin',) #  MemberFilter, 
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_active',
                                    'is_admin', 'is_staff', )}),  # 'member',
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # 'date_of_birth',
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',  # 'member',
            )}
         ),
    )
    search_fields = ('email', 'username', ) # 'member', 
    ordering = ('email', 'username', )  # 'member',
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
