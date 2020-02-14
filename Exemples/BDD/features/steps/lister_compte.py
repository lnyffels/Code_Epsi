from behave import *
from nose.tools import assert_equals, assert_list_equal, assert_set_equal

use_step_matcher("parse")
from Exemples.BDD import (client as clt, compte as c, operation as o)

@given("je suis connecté à mon application de getion de compte")
def step_impl(context):
    context.client = clt.Client('lnf', "azerty", '280373')

@when("je demande la liste de mes comptes")
def step_impl(context):
    context.liste_comptes = context.client.Comptes

@then("j'obtiens la liste suivante")
def step_impl(context):
    lst = []
    for row in context.table:
        lst.append(c.Compte(row["num_compte"], row["nom_compte"], row["type_compte"], float(row["interets"])))

    assert_list_equal(lst, context.liste_comptes)

