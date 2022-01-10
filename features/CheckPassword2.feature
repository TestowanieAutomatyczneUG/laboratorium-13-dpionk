Feature: PasswordChecker

	Klasa sprawdza, czy podany ciąg znaków spełnia wymagania prawidłowego hasła (co najmniej 8 znaków, 1 wielka litera,1 mała, cyfra i znak specjalny)

	Scenario: too short, no special characters and numbers
		Given there is a PasswordChecker
		When the password is "haslo"
		And we add upper letter
		Then the password is invalid.

	Scenario: no special characters, too short, no letters
		Given there is a PasswordChecker
		When the password is "54"
		And we add upper letter
		And we add number
		Then the password is invalid.
	
	Scenario: too short, no upper letters and numbers
		Given there is a PasswordChecker
		When the password is "df"
		And we add special character
		Then the password is invalid.

	Scenario: too short
		Given there is a PasswordChecker
		When the password is " "
		And we add lower letter
		Then the password is invalid.

	Scenario: too short, no upper letters and special characters
		Given there is a PasswordChecker
		When the password is "haslo"
		And we add number
		Then the password is invalid.

	Scenario: too short, no upper leters 
		Given there is a PasswordChecker
		When the password is "h"
		And we add number
		And we add special character
		Then the password is invalid.

	Scenario:
		Given there is a PasswordChecker
		When the password is "hasYTR"
		And we add number
		And we add upper letter
		And we add special character
		Then the password is valid.

	Scenario:
		Given there is a PasswordChecker
		When the password is "hASXLO45646"
		And we add number
		And we add lower letter
		And we add special character
		Then the password is valid.
