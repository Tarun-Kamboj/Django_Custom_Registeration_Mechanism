from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'gender', 'phone_no', 'prof_img', 'password1', 'password2', )


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")

class ImageForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('prof_img',)

    def clean_prof_img(self):
        prof_img = self.cleaned_data['prof_img']
        return prof_img



class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username', 'gender', 'phone_no', 'prof_img')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        return username

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        return gender

    def clean_phone_no(self):
        phone_no = self.cleaned_data['phone_no']
        return phone_no

    def clean_prof_img(self):
        prof_img = self.cleaned_data['prof_img']
        return prof_img
