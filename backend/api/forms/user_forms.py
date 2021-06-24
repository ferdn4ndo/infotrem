from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm

from api.models.user_model import User


class UserCreationForm(BaseUserCreationForm):

    class Meta(BaseUserCreationForm):
        model = User
        fields = ('email',)


class UserChangeForm(BaseUserChangeForm):

    class Meta(BaseUserChangeForm):
        model = User
        fields = ('email',)


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    readonly_fields = ('id',)
    form = UserChangeForm
    model = User
    list_display = [
        'id',
        'email',
        'name',
        'cpf',
        'city',
        'state',
        'zipcode',
        'phone',
        'is_admin',
        'is_staff',
        'is_active',
        'registered_at',
        'last_activity_at',
    ]
    list_filter = [
        'id',
        'email',
        'name',
        'cpf',
        'city',
        'state',
        'zipcode',
        'phone',
        'is_admin',
        'is_staff',
        'is_active',
        'registered_at',
        'last_activity_at',
    ]
    fieldsets = [
        [
            None,
            {
                'fields': [
                    'email',
                    'email_validated',
                    'email_validation_sent',
                    'email_validation_hash',
                    'name',
                    'cpf',
                    'birth_date',
                    'address',
                    'number',
                    'complement',
                    'city',
                    'state',
                    'zipcode',
                    'phone',
                ]
            }
        ],
        ['Permissions', {'fields': ['is_admin', 'is_staff', 'is_active']}],
    ]
    add_fieldsets = [
        [
            None,
            {
                'classes': ['wide'],
                'fields': ['email', 'password1', 'password2', 'is_admin', 'is_active']
            }
        ],
    ]
    search_fields = ['email', 'name', 'cpf']
    ordering = ['email', 'name', 'cpf']
