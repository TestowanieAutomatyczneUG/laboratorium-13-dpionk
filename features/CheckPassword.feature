Feature: CheckPassword

	Klasa sprawdza, czy podany ciąg znaków spełnia wymagania prawidłowego hasła (co najmniej 8 liter, 1 wielka litera, cyfra i znak specjalny)

	Scenario: password "k"
	Given there is a password checker
	When the password is just one lower letter
	Then the password is invalid

	Scenario: password "kF$4"
	Given there is a password checker
	When the password is less than 8 characters
	Then the password is invalid 

	Scenario: password "gdfgfd345435"
	Given there is a password checker
	When the password is more than 8 characters, at least one lower letter and number
	Then the password is invalid

	Scenario: password "sdfdFFFF5464565"
	Given there is a password checker
	When the password is more than 8 characters, at least one lower, upper letter and number
	Then the password is invalid

	Scenario: password "dsfsdFFFF$$$$2021"
	Given there is a password checker
	When the password is 8 characters, with lower, at least one lower, upper letter, special character and number
	Then the password is valid