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

# Kiểm tra đăng ký thành công
def test_Regis_01(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg1__E2fve').click()
    time.sleep(2)

    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")
    time.sleep(2)

    driver.find_element(By.ID, "register_taiKhoan").send_keys("giabao789")

    driver.find_element(By.ID, "register_matKhau").send_keys("giabao8910")

    driver.find_element(By.ID, "register_xacNhanMatKhau").send_keys("giabao8910")

    driver.find_element(By.ID, "register_hoTen").send_keys("baobao")

    driver.find_element(By.ID, "register_email").send_keys("baobaonek@gmail.com")

    driver.find_element(By.ID, "register_soDT").send_keys("0903214569")

    driver.find_element(By.CLASS_NAME, "ant-btn").click()

    message_success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Đăng ký thành công" in message_success.text

    assert "https://elearning-app-rm1o.vercel.app/users/dangnhap" in driver.current_url

def test_Regis_02(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg1__E2fve').click()
    time.sleep(2)

    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")

    driver.find_element(By.CLASS_NAME, "ant-btn").click()
    time.sleep(2)

    error_taiKhoan = driver.find_element(By.ID, "register_taiKhoan_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống tài khoản" in error_taiKhoan

    error_matKhau = driver.find_element(By.ID, "register_matKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống mật khẩu" in error_matKhau

    error_xacNhanMatKhau = driver.find_element(By.ID, "register_xacNhanMatKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống mật khẩu" in error_xacNhanMatKhau

    error_hoTen = driver.find_element(By.ID, "register_hoTen_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống họ tên" in error_hoTen

    error_email = driver.find_element(By.ID, "register_email_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Email không được để trống" in error_email

    error_soDT = driver.find_element(By.ID, "register_soDT_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Số điện thoại không được để trống" in error_soDT


def test_Regis_03(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg1__E2fve').click()
    time.sleep(2)

    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")

    driver.find_element(By.ID, "register_taiKhoan").send_keys("giabao789")

    driver.find_element(By.ID, "register_matKhau").send_keys("giabao8910")

    driver.find_element(By.ID, "register_xacNhanMatKhau").send_keys("giabao8910")

    driver.find_element(By.ID, "register_hoTen").send_keys("baobao")

    driver.find_element(By.ID, "register_email").send_keys("baobao1@gmail.com")

    driver.find_element(By.ID, "register_soDT").send_keys("0903214569")

    driver.find_element(By.CLASS_NAME, "ant-btn").click()
    time.sleep(2)

    message_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content")))

    assert "Tài khoản đã tồn tại" in message_element.text


def test_Regis_04(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg1__E2fve').click()
    time.sleep(2)

    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")
    driver.find_element(By.ID, "register_taiKhoan").send_keys("giabao7890")

    driver.find_element(By.ID, "register_matKhau").send_keys("giabao8910")

    driver.find_element(By.ID, "register_xacNhanMatKhau").send_keys("giabao8910")

    driver.find_element(By.ID, "register_hoTen").send_keys("baobao8910")

    driver.find_element(By.ID, "register_email").send_keys("baobao@gmail.com")

    driver.find_element(By.ID, "register_soDT").send_keys("0903214569")

    driver.find_element(By.CLASS_NAME, "ant-btn").click()
    time.sleep(2)

    message_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content")))
    assert "Email đã tồn tại" in message_element.text


def test_Regis_05(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg1__E2fve').click()
    time.sleep(2)

    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")

    driver.find_element(By.ID, "register_email").send_keys("baobao")

    driver.find_element(By.ID, "register_soDT").send_keys("5526")

    driver.find_element(By.ID, "register_matKhau").send_keys("giabao8910")

    driver.find_element(By.ID, "register_xacNhanMatKhau").send_keys("giabao")

    driver.find_element(By.CLASS_NAME, "ant-btn").click()
    time.sleep(2)

    # Expect result
    error_email = driver.find_element(By.ID, "register_email_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Email không chính xác" in error_email

    error_soDT = driver.find_element(By.ID, "register_soDT_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Số điện thoại không hợp lệ" in error_soDT

    error_xacNhanMatKhau = driver.find_element(By.ID, "register_xacNhanMatKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Mật khẩu không trùng khớp" in error_xacNhanMatKhau

