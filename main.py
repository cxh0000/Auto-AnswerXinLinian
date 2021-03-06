from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep
from os import remove
from os.path import exists
from parse_answer import *
from answer import *

user = input('username: ')
passwd = input('password: ')
browser = webdriver.Chrome()
browser.get('http://192.168.9.12/npels/')
wait = WebDriverWait(browser, 3)
current = 1  # 题号
ansll = []


def login(name, password):
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tbName'))).send_keys(name)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tbPwd'))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnLogin'))).click()


def intotest():
    try:
        browser.switch_to.frame('mainFrame')

        try:
            wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ctl00_cphContent_divWarning > div > div.homework_3 > ul > li.homework_3_2 > span > a'))).click()
        except TimeoutException:
            browser.close()
            print('没有测试!!!')
        sleep(1)
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                               '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl03_Action > span > input[type="button"]'))).click()
        except TimeoutException:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                               '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl04_Action > span > input[type="button"]'))).click()


        sleep(1)
    except TimeoutError:
        return intotest()


def answer_part_one():
    global ansll
    global current
    sleep(2)
    pageSource = browser.page_source
    with open('source.html', 'w+', encoding='utf-8') as f:
        f.write(pageSource)
    prase_result()
    ansll = callback(0)
    browser.switch_to.default_content()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#aPart1'))).click()
    browser.switch_to.frame('mainFrame')
    anlist = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                             'ul.choiceList > li > input')))

    flag = 1

    for item in anlist:
        if flag == 0:
            flag = 1
        if flag == 1 and 'A' == ansll[current - 1]:
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            item.click()
            flag = -4
            current += 1
        if flag == 2 and 'B' == ansll[current - 1]:
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            item.click()
            flag = -3
            current += 1
        if flag == 3 and 'C' == ansll[current - 1]:
            item.click()
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            flag = -2
            current += 1
        if flag == 4 and 'D' == ansll[current - 1]:
            item.click()
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            flag = -1
            current += 1

        flag += 1
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnNextPart'))).click()


def answer_part_two():
    global current, ansll
    anlist = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                             'ul.choiceList > li > input')))
    flag = 1
    for item in anlist:
        if flag == 0:
            flag = 1
        if flag == 1 and 'A' == ansll[current - 1]:
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            item.click()
            flag = -4
            current += 1
        if flag == 2 and 'B' == ansll[current - 1]:
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            item.click()
            flag = -3
            current += 1
        if flag == 3 and 'C' == ansll[current - 1]:
            item.click()
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            flag = -2
            current += 1
        if flag == 4 and 'D' == ansll[current - 1]:
            item.click()
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            flag = -1
            current += 1

        flag += 1
    try:
        section_b = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                '#form1 > div.content_test > div.class_mag.class_main_tab > div.test_frame > div:nth-child(7) > ul.test_list_2 > li > input')))
    except TimeoutException:
        print('没有找到Section B的内容')

    else:
        for item in section_b:
            item.clear()
            item.send_keys(ansll[current - 1])
            current += 1

    try:
        section_c = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                '#form1 > div.content_test > div.class_mag.class_main_tab > div.test_frame > div:nth-child(10) > ul > li > span > select')))
    except TimeoutException:
        section_c = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.test_frame > div:nth-child(7) > ul > li > span.test_match_2_2 > select')))

    for select in section_c:
        if ansll[current - 1] == 'A':
            Select(select).select_by_index(0)
            current += 1
        elif ansll[current - 1] == 'B':
            Select(select).select_by_index(1)
            current += 1
        elif ansll[current - 1] == 'C':
            Select(select).select_by_index(2)
            current += 1
        elif ansll[current - 1] == 'D':
            Select(select).select_by_index(3)
            current += 1
        elif ansll[current - 1] == 'E':
            Select(select).select_by_index(4)
            current += 1
        elif ansll[current - 1] == 'F':
            Select(select).select_by_index(5)
            current += 1
        elif ansll[current - 1] == 'G':
            Select(select).select_by_index(6)
            current += 1
        elif ansll[current - 1] == 'H':
            Select(select).select_by_index(7)
            current += 1
        elif ansll[current - 1] == 'I':
            Select(select).select_by_index(8)
            current += 1
        elif ansll[current - 1] == 'J':
            Select(select).select_by_index(9)
            current += 1
        elif ansll[current - 1] == 'K':
            Select(select).select_by_index(10)
            current += 1
        elif ansll[current - 1] == 'L':
            Select(select).select_by_index(11)
            current += 1
        elif ansll[current - 1] == 'M':
            Select(select).select_by_index(12)
            current += 1
        elif ansll[current - 1] == 'N':
            Select(select).select_by_index(13)
            current += 1
        elif ansll[current - 1] == 'O':
            Select(select).select_by_index(14)
            current += 1
        elif ansll[current - 1] == 'P':
            Select(select).select_by_index(15)
            current += 1
        elif ansll[current - 1] == 'Q':
            Select(select).select_by_index(16)
            current += 1
    if exists('EnglishAnswer.html'):
        remove('EnglishAnswer.html')
    if exists('source.html'):
        remove('source.html')


def main(user, passwd):
    login(user, passwd)
    intotest()
    answer_part_one()
    answer_part_two()


if __name__ == '__main__':
    main(user, passwd)
