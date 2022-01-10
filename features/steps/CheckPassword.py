from behave import *
from func.CheckPassword import CheckPassword

@given("there is a password checker")
def step_imp(context):
	context.checkPassword = CheckPassword()

@when("the password is just one lower letter")
def step_imp(context):
	context.password = "k"

@when("the password is less than 8 characters")
def step_imp(context):
	context.password = "kF$4"

@when("the password is more than 8 characters, at least one lower letter and number")
def step_imp(context):
	context.password = "gdfgfd345435"

@when("the password is more than 8 characters, at least one lower, upper letter and number")
def step_imp(context):
	context.password = "sdfdFFFF5464565"

@when("the password is 8 characters, with lower, at least one lower, upper letter, special character and number")
def step_imp(context):
	context.password = "dsfsdFFFF$$$$2021"

@then("the password is invalid")
def step_imp(context):
	assert context.checkPassword.ValidPassword(context.password) == False
@then("the password is valid")
def test_imp(context):
	assert context.checkPassword.ValidPassword(context.password) == True