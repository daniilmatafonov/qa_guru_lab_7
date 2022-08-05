import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.shared import browser

url = 'https://github.com'
search_element = '.header-search-input'
repo = 'yashaka/selene'
issue_tab = '#issues-tab'
issue_value = 'Set an attribute value via Selene'


@allure.tag('web', 'ui')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'yashaka')
@allure.feature('Testing github')
@allure.story(f'Find issue by name: {issue_value}')
@allure.link('https://github.com/yashaka', name='Owner')
def test_decorator_steps_with_label():
    open_page(url)
    search_repository(repo)
    go_to_repository(repo)
    open_issue_tab()
    should_see_issue_with_name(issue_value)


@allure.step(f'Open: {url}')
def open_page(url: str):
    browser.open(url)


@allure.step(f'Find repository: {repo}')
def search_repository(repo):
    browser.element(search_element).click()
    browser.element(search_element).send_keys(repo)
    browser.element(search_element).submit()


@allure.step(f'Choice repository: {repo}')
def go_to_repository(repository):
    browser.element(by.link_text(repository)).click()


@allure.step('Open tab Issues')
def open_issue_tab():
    browser.element(issue_tab).click()


@allure.step(f'Check Issue with name: {issue_value}')
def should_see_issue_with_name(issue_value):
    browser.element(by.partial_text(issue_value)).click()