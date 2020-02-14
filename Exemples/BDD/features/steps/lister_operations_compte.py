from behave import *
from nose.tools import assert_equals

use_step_matcher("parse")

@given("je dispose du compte courant_123")
def step_impl(context):
    pass


@when("je souhaite obtenir la liste de mes opérations des trente derniers jours")
def step_impl(context):
    pass

@then("le systeme me donne la liste des dernieres operations triées par date")
def step_impl(context):
    tb = context.table[1]
    print(tb["description"])