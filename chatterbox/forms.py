from django import forms
from .models import Banter,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture")
    profile_bio  = forms.CharField(label='', required=False , widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':' Profile Bio'}))
    profile_link = forms.CharField(label='', required=False ,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' Website Link'}))
    facebook_link = forms.CharField(label='', required=False ,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Facebook Link'}))
    instagram_link = forms.CharField(label='', required=False ,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Instagram Link'}))
    linkdlen_link = forms.CharField(label='', required=False ,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' Linkdlen Link'}))
    class Meta:
        model = Profile
        fields = ('profile_image', 'profile_bio', 'profile_link', 'facebook_link','instagram_link','linkdlen_link',)
        

class BanterForm(forms.ModelForm):
	body = forms.CharField(required=True, 
		widget=forms.widgets.Textarea(
			attrs={
			"placeholder": "Enter Your Musker Meep!",
			"class":"form-control",
			}
			),
			label="",
		)

	class Meta:
		model = Banter
		exclude = ("user", "likes",)       
        
class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
	
	def clean_username(self):
		username = self.cleaned_data.get('username')
		# If an instance exists and the username hasn't changed, skip duplicate check
		if self.instance.pk and self.instance.username == username:
			return username
		# Otherwise, enforce the uniqueness check
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("Username already exists.")
		return username
