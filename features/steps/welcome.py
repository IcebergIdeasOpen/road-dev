from behave import *

use_step_matcher("re")


@given("Monique is on the welcome page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Monique is on the welcome page')


@when("She selects the book recommendation button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When She selects the book recommendation button')


@then("Monique see the book Extreme Programming Installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Monique see the book Extreme Programming Installed')