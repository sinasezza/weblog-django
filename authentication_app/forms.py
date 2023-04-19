from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth import password_validation , authenticate
from . import models


class AdminPanelUserCreationForm(UserCreationForm):
    
    class meta(UserCreationForm):
        model = models.AuthUser
        fields = UserCreationForm.Meta.fields + ('profile_photo','age','bio','phone_number',)

# ------------------------------------

class AdminPanelUserChangeForm(UserChangeForm):

    class meta(UserChangeForm):
        model = models.AuthUser
        fields = UserChangeForm.Meta.fields
        
# ------------------------------------

class UserSignupForm_Step01(forms.ModelForm):

    class Meta:
        model  = models.AuthUser
        fields = ['username','phone_number']

    password1    = forms.CharField(label="Password",)
    password2    = forms.CharField(
        label="Password confirmation",
        help_text="Enter the same password as before, for verification.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['phone_number'].required = True
        self.fields['password1'].required = True
        self.fields['password2'].required = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
        
# ------------------------------------

class UserSignupForm_Step02(forms.ModelForm):
    class Meta:
        model = models.AuthUser
        fields = ['first_name','last_name','email','age','bio']

# ------------------------------------

class UserSignupForm_Step03(forms.ModelForm):
    class Meta:
        model  = models.AuthUser
        fields = ['profile_photo']   
        
# ------------------------------------

class UserChangeProfileForm(forms.ModelForm):
    new_password = forms.CharField(max_length=30)
    
    class Meta:
        model = models.AuthUser
        fields = ['username','first_name','last_name','new_password','phone_number',
            'email','age','bio','profile_photo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['phone_number'].required = True
        self.fields['new_password'].required = False

    
    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["new_password"]:
            user.set_password(self.cleaned_data["new_password"])
        if commit:
            user.save()
        return user