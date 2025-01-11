from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class customRegistrationForm(UserCreationForm):
    """Registration Form"""

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'date_of_birth', 'address']

    def __init__(self, *args, **kwargs):
        self.episode = kwargs.pop("episode", None)
        super().__init__(*args, **kwargs)
        self.fields["username"].label = False
        self.fields["first_name"].label = False
        self.fields["last_name"].label = False
        self.fields["email"].label = False
        self.fields["phone"].label = False
        self.fields["date_of_birth"].label = False
        self.fields["address"].label = False
        self.fields["password1"].required = False
        self.fields["password2"].required = False

    def clean_username(self):
        username = self.cleaned_data.get('username')
        model = self.Meta.model
        user = model.objects.filter(username__iexact=username)

        if user.exists():
            raise forms.ValidationError("A user with that name already exists")

        return self.cleaned_data.get('username')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        model = self.Meta.model
        user = model.objects.filter(email__iexact=email)
        if user.exists():
            raise forms.ValidationError("A user with that email already exists")

        return self.cleaned_data.get('email')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confim_password = self.data.get('confirm_password')

        if password != confim_password:
            raise forms.ValidationError("Passwords do not match")

        return self.cleaned_data.get('password')

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        if dob > datetime.now().date():
            raise forms.ValidationError("The date of birth cannot be in the future.")
        return dob

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()
        return instance


class customLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
