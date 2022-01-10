from behave import *
from func.CheckPassword import CheckPassword

@given("there is a PasswordChecker")
def step_imp(context):
	context.password_checker = CheckPassword()

@when('the password is "{text}"')
def step_impl(context, text):
	context.password = text

@when("we add lower letter")
def step_impl(context):
	context.password += "k"

@when("we add special character")
def step_impl(context):
	context.password += "$"

@when("we add number")
def step_impl(context):
	context.password += "7"
	
@when("we add upper letter")
def step_impl(context):
	context.password += "T"

@then("the password is invalid.")
def step_imp(context):
	assert context.password_checker.ValidPassword(context.password) == False
@then("the password is valid.")
def test_imp(context):
	assert context.password_checker.ValidPassword(context.password) == True