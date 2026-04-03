from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class VetOfficerSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=50,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
		
	email = forms.EmailField(
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				'placeholder': 'Email',
				'class': 'form-control'
			}
		)
	)
	registration_number=forms.CharField(label='KVB Number')
	licence_number=forms.CharField(label='Licence Number')
	specialization=forms.ChoiceField(choices=[('large', 'Large Animals'), ('small', 'Small Animals')], label='Select Specialization')
	vet_category=forms.ChoiceField(choices=[('surgeon', 'Surgeon'), ('Technologist Degree', 'Technologist Degree'),('Technologist Diploma', 'Technologist Diploma'),('Technician', 'Technician')], label='Select Vet Category')
	supervisor=forms.CharField(label='Supervisor')
	business_name=forms.CharField(label='Business Name')
	county=forms.CharField()
	subcounty=forms.CharField()
	location=forms.CharField()
	phone_number = forms.RegexField(regex='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', max_length=13)
	password1 = forms.CharField(
		label='Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'class': 'form-control'
			}
		)
	)
	password2 = forms.CharField(
		label='Confirm Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Confirm Password',
				'class': 'form-control'
			}
		)
	)
	
	
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username','first_name','last_name','registration_number','licence_number','specialization','vet_category','supervisor','business_name','county','subcounty','location','phone_number','email','password1', 'password2',)

	
class FarmerSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=50,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
	email = forms.EmailField()
	phone_number = forms.RegexField(regex='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', max_length=13)
	farm_name  = forms.CharField(max_length=20)
	county=forms.CharField(label='County')
	location = forms.CharField(max_length=30)
	password1 = forms.CharField(
		label='Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'class': 'form-control'
			}
		)
	)

	password2 = forms.CharField(
		label='Confirm Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Confirm Password',
				'class': 'form-control'
			}
		)
	)
	
	
	
	


	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username','first_name','last_name','farm_name','email','phone_number','county', 'location','password1', 'password2']
			

class OfficialSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=50,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
		
	email = forms.EmailField(
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				'placeholder': 'Email',
				'class': 'form-control'
			}
		)
	)
	phone_number = forms.RegexField(regex='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', max_length=13)
	county=forms.CharField()
	sub_county=forms.CharField()
	employment_number=forms.CharField()
	designation=forms.ChoiceField(choices=[('director', 'Director'), ('svco', 'Svco')], label='Select Designation')

	

	
	password1 = forms.CharField(
		label='Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'class': 'form-control'
			}
		)
	)

	password2 = forms.CharField(
		label='Confirm Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Confirm Password',
				'class': 'form-control'
			}
		)
	)
	
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username','first_name','last_name','phone_number','county','sub_county','registration_number','employment_number','designation','email','password1', 'password2',)

class CooperativeSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=50,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
		
	email = forms.EmailField(
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				'placeholder': 'Email',
				'class': 'form-control'
			}
		)
	)
	phone_number = forms.RegexField(regex='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', max_length=13)
	county=forms.CharField()
	sub_county=forms.CharField()
	cooperative_name=forms.CharField()
	reg_no=forms.CharField()
	designation=forms.ChoiceField(choices=[('chairman', 'Chairman'), ('secretary', 'Secretary'),('treasurer', 'Treasurer')], label='Select Designation')




	password1 = forms.CharField(
		label='Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'class': 'form-control'
			}
		)
	)

	password2 = forms.CharField(
		label='Confirm Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Confirm Password',
				'class': 'form-control'
			}
		)
	)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username','first_name','last_name','phone_number','county','sub_county','cooperative_name','reg_no','designation','email','password1', 'password2',)

