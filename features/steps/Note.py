from behave import *
from assertpy import assert_that
from func.Note import Note 

@when("trying to create a note with none as a name")
def step_imp(context):
	context.noteName = None
	context.noteValue = 2.0

@when("trying to create a note with an empty string as name")
def step_imp(context):
	context.noteName = ''
	context.noteValue = 2.0

@when("trying to create a note with a different datatype than string as name")
def step_imp(context):
	context.noteName = {}
	context.noteValue = 2.0

@when("trying to create a note with a non empty string as name")
def step_imp(context):
	context.noteName = "notatka"
	context.noteValue = 2.0

@when("trying to create a note with a different datatype than float as note")
def step_imp(context):
	context.noteName = "notatka"
	context.noteValue = 5656

@when("trying to create a note with a value less than 2 as note")
def step_imp(context):
	context.noteName = "notatka"
	context.noteValue = 1.0

@when("trying to create a note with a value more than 6 as note")
def step_imp(context):
	context.noteName = "notatka"
	context.noteValue = 7.67

@when("trying to create a note with a value more than 2 and less than 6 as note")
def step_imp(context):
	context.noteName = "notatka"
	context.noteValue = 5.60


@then("the note won't be created")
def step_imp(context):
	assert_that(Note).raises(Exception).when_called_with(context.noteName, context.noteValue)

@then("Note will be created")
def step_imp(context):
	assert Note(context.noteName, context.noteValue).getName() == context.noteName
