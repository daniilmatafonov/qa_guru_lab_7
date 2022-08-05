import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

url = 'https://github.com'
search_element = '.header-search-input'
repo = 'yashaka/selene'
issue_tab = '#issues-tab'
issue_value = 'Set an attribute value via Selene'


def test_dynamic_steps():
    with allure.step(f'Open: {url}'):
        browser.open(url)

    with allure.step(f'Find repository: {repo}'):
        browser.element(search_element).click()
        browser.element(search_element).send_keys(repo)
        browser.element(search_element).submit()

    with allure.step(f'Choice repository: {repo}'):
        browser.element(by.link_text(repo)).click()

    with allure.step('Open tab Issues'):
        browser.element(issue_tab).click()

    with allure.step(f'Check Issue with name: {issue_value}'):
        browser.element(by.partial_text(issue_value)).should(be.visible)
