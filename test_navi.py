import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from test_login import test_Login_01, test_Login_04

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_Navi_01(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    element = driver.find_element(By.XPATH, "//a[text()='Danh mục khoá học']")
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(5)

    driver.find_element(By.XPATH, "//a[text()='Lập trình Backend']").click()
    time.sleep(5)

def test_Navi_02(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[text()='Khoá học']").click()
    time.sleep(2)


def test_Navi_03(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[text()='Khoá học']").click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "navbar-brand").click()
    time.sleep(2)

def test_Navi_04(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "button_buttonBg2__7Y8fh").click()
    time.sleep(5)

def test_Navi_05(driver):
    test_Login_01(driver)
    driver.find_element(By.CLASS_NAME, "userDropdown_dropdownTrigger__TO32H").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "userDropdown_dropdownMenu__6DtQw"))
    )
    driver.find_element(By.XPATH, "//a[text()='Thông tin']").click()

    titleProfile = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "thongtintaikhoan_profTitle__Y4ntt"))
    )

    assert EC.visibility_of_all_elements_located((By.CLASS_NAME, "thongtintaikhoan_profTitle__Y4ntt"))

