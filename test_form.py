import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_login import test_Login_01
from test_navi import test_Navi_05
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def clear_field(element):
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.BACKSPACE)


def test_Form_01(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg2__7Y8fh').click()
    time.sleep(2)

    driver.find_element(By.ID, "TuVan_name").send_keys("Gia Bảo")

    driver.find_element(By.ID, "TuVan_email").send_keys("baobao@gmail.com")

    driver.find_element(By.ID, "TuVan_phone").send_keys("0936589632")

    driver.find_element(By.XPATH, "//button[@id='btnTuVan']").click()
    time.sleep(2)


def test_Form_02(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg2__7Y8fh').click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='btnTuVan']").click()
    time.sleep(2)

    error_hoten = driver.find_element(By.ID, "TuVan_name_help").find_element(By.CLASS_NAME,
                                                                             "ant-form-item-explain-error").text
    assert "Không được để trống tên" in error_hoten

    error_email = driver.find_element(By.ID, "TuVan_email_help").find_element(By.CLASS_NAME,
                                                                              "ant-form-item-explain-error").text
    assert "Không được để trống email" in error_email

    error_soDT = driver.find_element(By.ID, "TuVan_phone_help").find_element(By.CLASS_NAME,
                                                                             "ant-form-item-explain-error").text
    assert "Không được để trống số điện thoại" in error_soDT


def test_Form_03(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'button_buttonBg2__7Y8fh').click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='TuVan_email']").send_keys('baobao')
    driver.find_element(By.XPATH, "//*[@id='TuVan_phone']").send_keys('09923')

    error_email = driver.find_element(By.ID, "TuVan_email_help").find_element(By.CLASS_NAME,
                                                                              "ant-form-item-explain-error").text
    assert "Email không hợp lệ" in error_email

    error_soDT = driver.find_element(By.ID, "TuVan_phone_help").find_element(By.CLASS_NAME,
                                                                             "ant-form-item-explain-error").text
    assert "Số điện thoại phải từ 7 - 11 chữ số!" in error_soDT


def test_Form_04(driver):
    test_Navi_05(driver)
    time.sleep(2)

    ho_ten_element = driver.find_element(By.ID, "nest-messages_hoTen")
    email_element = driver.find_element(By.ID, "nest-messages_email")
    soDT_element = driver.find_element(By.ID, "nest-messages_soDT")
    matKhau_element = driver.find_element(By.ID, "nest-messages_matKhau")

    clear_field(ho_ten_element)
    clear_field(email_element)
    clear_field(soDT_element)
    clear_field(matKhau_element)

    ho_ten_element.send_keys("baobao1")
    email_element.send_keys("baobaotester@gmail.com")
    soDT_element.send_keys("0908968765")
    matKhau_element.send_keys("tester1234")

    driver.find_element(By.XPATH, "//button[span[text() = 'Cập nhật thông tin']]").click()


def test_Form_05(driver):
    # Steps
    test_Navi_05(driver)
    time.sleep(2)
    email_element = driver.find_element(By.ID, "nest-messages_email")
    soDT_element = driver.find_element(By.ID, "nest-messages_soDT")
    matKhau_element = driver.find_element(By.ID, "nest-messages_matKhau")

    clear_field(email_element)
    clear_field(soDT_element)
    clear_field(matKhau_element)

    email_element.send_keys("baobaotester")
    soDT_element.send_keys("090de")
    matKhau_element.send_keys("tes")

    driver.find_element(By.XPATH, "//button[span[text() = 'Cập nhật thông tin']]").click()
    time.sleep(2)

    # Expected result
    error_email = driver.find_element(By.ID, "nest-messages_email_help").find_element(By.CLASS_NAME,
                                                                                      "ant-form-item-explain-error").text
    assert "Email không hợp lệ!" in error_email

    error_soDT = driver.find_element(By.ID, "nest-messages_soDT_help").find_element(By.CLASS_NAME,
                                                                                    "ant-form-item-explain-error").text
    assert "Số điện thoại không hợp lệ!" in error_soDT

    error_pwd = driver.find_element(By.ID, "nest-messages_matKhau_help").find_element(By.CLASS_NAME,
                                                                                      "ant-form-item-explain-error").text
    assert "Mật khẩu phải từ 6 đến 20 ký tự!" in error_pwd


