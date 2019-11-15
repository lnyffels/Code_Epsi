from behave import *
from nose.tools import assert_equals


use_step_matcher("re")



@given("I have 2 departments in a list MaList")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.ma_list = []
    context.my_number = 0
    context.ma_list.append("Depart1")
    context.ma_list.append("Depart2")


@when("I count each items")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_number = context.ma_list.__len__()


@then("I should have two in number")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_equals(context.my_number, 2)
