from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from conf import fields

from users.models import User, UserProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', )


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = fields.USER_PROFILE_FIELDS

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()

        return user_profile