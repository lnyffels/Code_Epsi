from behave import *
from nose.tools import assert_equals
from Exemples.BDD.compte import Compte
from Exemples.BDD.operation import Operation


use_step_matcher("parse")

@given("mon compte courant_123 a un solde de {montant:f} euros")
def step_impl(context, montant):
    context.courant_123 = Compte(123, "courant 123")
    context.courant_123.ajouter_operation(Operation(montant, "dépot initial", "C"))


@when("je credite mon compte courant_123 de {montant_credit:f} euros")
def step_impl(context, montant_credit):
    context.courant_123.ajouter_operation(Operation(montant_credit, "dépot initial", "C"))

@then("le solde de mon compte courant_123 est de {solde:f} euros")
def step_impl(context, solde):
    solde_compte = context.courant_123.donner_solde()
    assert_equals(solde_compte, solde)