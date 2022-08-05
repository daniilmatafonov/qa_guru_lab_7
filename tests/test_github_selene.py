from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

url = 'https://github.com'
search_element = '.header-search-input'
repo = 'yashaka/selene'
issue_tab = '#issues-tab'
issue_value = 'Set an attribute value via Selene'


def test_selene():
    browser.open(url)
    browser.element(search_element).click()
    browser.element(search_element).send_keys(repo)
    browser.element(search_element).submit()
    browser.element(by.link_text(repo)).click()
    browser.element(issue_tab).click()
    browser.element(by.partial_text(issue_value)).should(be.visible)


