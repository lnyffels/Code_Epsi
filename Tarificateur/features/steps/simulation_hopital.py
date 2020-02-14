from behave import *
from nose.tools import assert_equals
from Tarificateur.model.request import Request
from Tarificateur.model.simulateur import Simulateur

use_step_matcher("re")


@given("je ne releve pas du régime Alsace Moselle")
def step_impl(context):
    context.req = Request()
    context.req.regime_alsace_moselle = False


@given("mon médécin Le médecin a adhéré à un Dispositif de Pratique TArifaire Maitrisée")
def step_impl(context):
    context.req.dptam = True

@given("ma prestation choisi (?P<prestation>.+)")
def step_impl(context, prestation):
    context.req.prestation = prestation


@given("Le montant simulé pour mes dépense est (?P<depenses>.+) euros")
def step_impl(context, depenses):
    context.req.depenses = float(depenses)


@given("la formule AXA choisit est (?P<formule>.+)")
def step_impl(context, formule):
    context.req.formule = formule


@when("Je calcule mes remboursements")
def step_impl(context):
    sim = Simulateur(context.req)
    context.res = sim.calculer_remboursements()


@then("la base de remboursement Sécurité sociale est de (?P<base_secu>.+) euros")
def step_impl(context, base_secu):
    assert_equals(float(base_secu), float(context.res.base_secu))

@step("le reste à charge avant la formule AXA est de (?P<rac_avant_axa>.+) euros")
def step_impl(context, rac_avant_axa):
    assert_equals(float(rac_avant_axa), float(context.res.rac_avant_axa))


@step("le remboursement AXA plus Sécu est de (?P<axa_plus_secu>.+) euros")
def step_impl(context, axa_plus_secu):
    assert_equals(float(axa_plus_secu), float(context.res.axa_plus_secu))


@step("le reste à charge est de (?P<rac_prospect>.+) euros")
def step_impl(context, rac_prospect):
    assert_equals(float(rac_prospect), float(context.res.rac_prospect))