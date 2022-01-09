import re


class CheckPassword:

	def ValidPassword(self,password):
		if type(password) is str :
			pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})"
			if re.match(pattern, password):
				return True
			return False
		else:
			raise Exception("Wrong type of argument")