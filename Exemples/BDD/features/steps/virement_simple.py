from behave import *
from Exemples.BDD.compte import Compte
from Exemples.BDD.compte_virer_usecase import CompteVirerUsecase
from Exemples.BDD.operation import Operation
from nose.tools import assert_equals, assert_raises

use_step_matcher("parse")


@given("mon compte courant_123 a un solde de {init_montant_courant:f} euros")
def step_impl(context, init_montant_courant):
    context.courant_123 = Compte(123, "courant 123")
    context.courant_123.ajouter_operation(Operation(init_montant_courant, "dépot initial", "C"))


@given("mon compte epargne_CEL a un solde de {init_montant_epargne:f} euros")
def step_impl(context, init_montant_epargne):
    context.epargne = Compte(456, "CEL")
    context.epargne.ajouter_operation(Operation(init_montant_epargne, "dépot initial epargne", "C"))


@when("je vire {montant:f} euros de mon compte courant_123 vers mon compte epargne_CEL")
def step_impl(context, montant):
    context.uc = CompteVirerUsecase()
    context.uc.transfer(montant, context.courant_123, context.epargne)


@step("alors mon compte courant_123 a un solde de {solde_courant:f} euros")
def step_impl(context, solde_courant):
    solde_compte = context.courant_123.donner_solde()
    assert_equals(solde_compte, solde_courant)




@then("mon compte epargne_CEL a un solde de {solde_epargne:f} euros")
def step_impl(context, solde_epargne):
    solde_compte = context.epargne.donner_solde()
    assert_equals(solde_compte, solde_epargne)