"""
* - - - - - - - - - - - - - - - - - - - - - - - - - *
|                 FUNCTIONAL  TESTS                 |
|                 FOR BOOK PROJECTS                 |
|                                                   |
|    AUTHOR: COLLEEN BERNUM     DATE: 10/04/2016    |
|    FILENAME: functional_tests.py                  |
|                                                   |
* - - - - - - - - - - - - - - - - - - - - - - - - - *

"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
