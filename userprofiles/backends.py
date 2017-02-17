from django.contrib.auth.models import User

class EmailBackend(object):
	def authenticate(self, email=None, password=None):
		try:
			# Tratar de traer el usuario con el email
			user = User.objects.get(email=email)
			#Si existe tiene que verificar que el password sea el que se envia desde el formulario
			if user.check_password(password):
				# Si el password es correcto retorno el usuario
				return user
				# Si no es correcta retorna un DoesNot Exist del usuario y retorna None
		except User.DoesNotExist:
			return None

	def get_user(self, user_id):
		# Intentar buscar un usuario con el id indicado
		try:
			return User.objects.get(id=user_id)
		# Sino lo encuentra entonces retorna None
		except User.DoesNotExist:
			return None