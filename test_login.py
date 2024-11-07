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

def test_Login_01(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg1__E2fve').click()
    time.sleep(2)

    driver.find_element(By.ID, "login-form_taiKhoan").send_keys("giabao789")

    driver.find_element(By.ID, "login-form_matKhau").send_keys("giabao8910")

    driver.find_element(By.ID, "login-button").click()

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Đăng nhập thành công" in message_element.text
    assert "https://elearning-app-rm1o.vercel.app/" in driver.current_url
    assert driver.find_element(By.ID, "userDropdown")



def test_Login_02(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg1__E2fve').click()
    time.sleep(2)

    driver.find_element(By.ID, "login-form_taiKhoan").send_keys("giabao78")

    driver.find_element(By.ID, "login-form_matKhau").send_keys("giabao89")

    driver.find_element(By.ID, "login-button").click()

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    message_text = message_element.text
    assert "Tài khoản hoặc mật khẩu không đúng" in message_text

def test_Login_03(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg1__E2fve').click()
    time.sleep(2)

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_taiKhoan = driver.find_element(By.ID, "login-form_taiKhoan_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống tài khoản" in error_taiKhoan

    error_matKhau = driver.find_element(By.ID, "login-form_matKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống mật khẩu" in error_matKhau


def test_Login_04(driver):
    test_Login_01(driver)
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "ant-dropdown-trigger").click()
    time.sleep(2)

    driver.find_element(By.ID, "button-logout").click()

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "đăng xuất thành công" in message_element.text

    assert "https://elearning-app-rm1o.vercel.app/" in driver.current_url

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Đăng nhập']"))
    )
    assert driver.find_element(By.XPATH, "//a[text()='Đăng nhập']")

def test_Login_05(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg1__E2fve').click()
    time.sleep(2)

    driver.find_element(By.ID, "login-form_taiKhoan").send_keys("bbb111")

    driver.find_element(By.ID, "login-form_matKhau").send_keys("123456")

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Đăng nhập thành công" in message_element.text

    assert "https://elearning-app-rm1o.vercel.app/" in driver.current_url
    time.sleep(2)

    driver.find_element(By.ID, "userDropdown").click()
    time.sleep(2)

    assert driver.find_element(By.XPATH, "//a[text()='Trang quản trị']")