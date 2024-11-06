import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Testcase 1: Tìm kiếm thành công
def test_Search_01(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm']").send_keys('java')

    driver.find_element(By.CLASS_NAME, "search_btn").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "timkiem_card__ZulPx"))
    )
    assert driver.find_element(By.CLASS_NAME, "timkiem_card__ZulPx")

def test_Search_02(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@class='btn my-2 my-sm-0 search_btn button_buttonSearch__PebGO']").click()
    time.sleep(2)

def test_Search_03(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm']").send_keys('@@@@')
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "search_btn").click()
    # Expected result
    no_course_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Không có khóa học nào']"))
    )
    assert no_course_message.is_displayed()


def test_Search_04(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm']").send_keys('hsdhsạdahsjdháhdsahdhadhsạdhahh')
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "search_btn").click()
    # Expected result
    no_course_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Không có khóa học nào']"))
    )
    assert no_course_message.is_displayed()