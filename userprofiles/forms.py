from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username', 'email')

class EmailAuthenticationForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(label='Passowrd', widget=forms.PasswordInput)

	# Metodo constructor
	def __init__(self, *args, **kwargs):
		self.user_cache = None
		# Super es el padre de la clase
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)


	def clean(self):
		# Obtenemos el email y el password
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		# Tratar de encontrar un usuario con este email
		self.user_cache = authenticate(email=email, password=password)

		# Authenticate retorna(2 valores) None o el valor que encuentra

		# Si user_cache es None significa que no existe y levantamos un error de validacion de formulario
		if self.user_cache is None:
			raise forms.ValidationError('Usuario incorrecto')
		# Si el usuario existe validamos que este activo, sino esta activo levantamos un error
		elif not self.user_cache.is_active:
			raise forms.ValidationError('Usuario inactivo')

		# Si el usuario existe y esta activo retorna cleaned data y almacenamos el usuario en user_cache
		return self.cleaned_data

	# Obtenemos el usuario y lo retorna
	def get_user(self):
		return self.user_cache
# mayte carranco

