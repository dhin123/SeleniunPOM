class Loginpage:
    username_id  = "Email"
    password_id = "Password"
    login_xpath = "//input[@class='button-1 login-button']"

    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def login(self):
        self.driver.find_element_by_xpath(self.login_xpath).click()
