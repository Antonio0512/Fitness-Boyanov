from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

Member = get_user_model()


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username', 'class': 'form-control mb-2'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email', 'class': 'form-control mb-2'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password', 'class': 'form-control mb-2'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm Password', 'class': 'form-control mb-2'})

    class Meta:
        model = Member
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username', 'class': 'form-control mb-2'})
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Password', 'class': 'form-control mb-2'})

    class Meta:
        fields = ('username', 'password')


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Member
        fields = ("username", "first_name", "last_name", "email", "phone_number", "age", "profile_picture")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username', 'class': 'form-control mb-2'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email', 'class': 'form-control mb-2'})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'First name', 'class': 'form-control mb-2'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Last name', 'class': 'form-control mb-2'})
        self.fields['phone_number'].widget.attrs.update(
            {'placeholder': 'Phone number', 'class': 'form-control mb-2'})
        self.fields['age'].widget.attrs.update(
            {'placeholder': 'Age', 'class': 'form-control mb-2'})