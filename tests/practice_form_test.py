import allure
from allure_commons.types import Severity

from demoqa_tests.model.pages.practice_form import Form
from demoqa_tests.data.user_data import kirill_k


@allure.title("Successful filled form")
def test_submitting_form():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'kirill_k')
    allure.dynamic.feature('Successful filled form')

    form = Form()

    with allure.step('submit_form'):
        form.submit_form(kirill_k)

    with allure.step('validate_form'):
        form.validate_form(kirill_k)
