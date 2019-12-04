from behave import *

use_step_matcher("re")


@given("mon compte epargne_CEL a un solde de 1200\.00 euros")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given mon compte epargne_CEL a un solde de 1200.00 euros')


@when("je vire 100 euros de mon compte courant_123 vers mon compte epargne_CEL")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When je vire 100 euros de mon compte courant_123 vers mon compte epargne_CEL')


@then("alors mon compte courant_123 a un solde de 180\.50")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then alors mon compte courant_123 a un solde de 180.50')