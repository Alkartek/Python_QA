from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLK:
    def test_swipe_to_lk(self, driver):
        current_url = driver.current_url

        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.NAME, "name").send_keys("alkartek5456788@gmail.com")
        driver.find_element(By.NAME, "Пароль").send_keys("5456788")
        driver.find_element(
            By.XPATH,
            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
        ).click()
        WebDriverWait(driver, 5).until(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
        assert current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        assert WebDriverWait(driver, 5).until(EC.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))


    def test_swipe_to_burger(self, driver):
        current_url = driver.current_url

        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.NAME, "name").send_keys("alkartek5456788@gmail.com")
        driver.find_element(By.NAME, "Пароль").send_keys("5456788")
        driver.find_element(
            By.XPATH,
            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
        ).click()
        WebDriverWait(driver, 500).until(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
        assert current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        assert WebDriverWait(driver, 500).until(
            EC.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))

        driver.find_element(By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2']")
        assert current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_choose_burger_ingridient(self, driver):
        current_url = driver.current_url

        WebDriverWait(driver, 50).until(EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))
        driver.find_element(By.XPATH, "//span[text() = 'Начинки']").click()
        WebDriverWait(driver,50)
        driver.find_element(By.XPATH, "//span[text() = 'Булки']").click()
        WebDriverWait(driver,50)
        driver.find_element(By.XPATH, "//span[text() = 'Соусы']").click()


        # driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[3]").click()
        # WebDriverWait(driver,50)
        # driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[1]").click()
        # WebDriverWait(driver, 50)


