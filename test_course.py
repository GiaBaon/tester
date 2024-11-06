import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from test_login import test_Login_01
from test_navi import test_Navi_02

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_Course_01(driver):
    test_Navi_02(driver)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[@id='btn_DangKy_KH']").click()
    time.sleep(5)

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Vui lòng đăng nhập để đăng ký khoá học" in message.text

    assert "https://elearning-app-rm1o.vercel.app/users/dangnhap" in driver.current_url

def test_Course_02(driver):
    test_Login_01(driver)
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "nav-link header_navLink__orUFa ").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='btn_DangKy_KH']").click()
    time.sleep(2)

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    message_text = message_element.text
    assert "Đăng ký thành công" in message_text


def test_DKKH_003(driver):
    # Steps
    test_Login_01(driver)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "nav-link header_navLink__orUFa ").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='btn_DangKy_KH']").click()
    time.sleep(2)

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    message_text = message_element.text
    assert "Đã đăng ký khóa học này rồi!" in message_text