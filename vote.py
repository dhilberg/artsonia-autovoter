"""
Very simple application that uses Selenium to repeatedly load the Artsonia artist of the week page
for a certain age range and vote for one of the entries.
"""

import os
from selenium import webdriver

log_directory = os.path.join(os.getcwd(), '.logs')
log_path = os.path.join(log_directory, 'geckodriver.log')

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

geckodriver_path = os.path.join(os.getcwd(), 'geckodriver.exe')

browser = webdriver.Firefox(executable_path=geckodriver_path, service_log_path=log_path)

count = 1
max_count = 6
while count < max_count:
    print(f'Vote attempt {count} of {max_count - 1}')

    # Artsonia uses cookies to track your voting. Deleting the cookies allows you to re-vote.
    browser.delete_all_cookies()

    browser.get('http://www.artsonia.com/aotw/vote/fan-direct/84806714')
    browser.find_element_by_id('BtnVote_84806714').click()
    count += 1

browser.quit()
