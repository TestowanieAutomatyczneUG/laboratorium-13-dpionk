from behave import *
from func.Note import Note


def before_scenario(context, scenario):
    context.note = Note()


def after_scenario(context, scenario):
    context.note = None