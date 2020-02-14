from behave import *

use_step_matcher("re")



@given("J'ai un compte_A avec un solde de 1000 euros")
def step_impl(context):
   context.compte_A = Compte()
   context.compte_A.solde = 1000

@given("J'ai un compte_B avec un solde de 0 euros")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given J\'ai un compte_B avec un solde de 0 euros')


@when("Je vire 150\.00 euros du compte_A vers le compte_B")
def step_impl(context):
    raise NotImplementedError(u'STEP: When Je vire 150.00 euros du compte_A vers le compte_B')


@then("le solde de mon compte_A est de 850\.00 euros")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then le solde de mon compte_A est de 850.00 euros')


@step("le solde de mon compte_B est de 150\.00 euros")
def step_impl(context):
    raise NotImplementedError(u'STEP: And  le solde de mon compte_B est de 150.00 euros')


@step("le virement est confirmé")
def step_impl(context):
    raise NotImplementedError(u'STEP: And le virement est confirmé')