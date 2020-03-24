from selenium import webdriver
from time import sleep
from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.tinder.com")

        sleep(5)

        # click login via facebook button
        # try:
        fb_login = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_login.click()
        # except Exception:
        #     try:
        #         more_options = self.driver.find_element_by_xpath()

        # switch to login window
        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])

        # enter facebook login email
        fb_email = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_email.send_keys(username)

        # enter facebook login password
        fb_pass = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_pass.send_keys(password)

        # click login button
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        # switch back to base window
        self.driver.switch_to_window(base_window)

        sleep(3)

        # close first popup
        popup_1 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        sleep(3)

        # close second popup
        popup_2 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    # swipe right
    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    # swipe left
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    # make it auto swipe right
    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.out_of_likes()
                        print('You are out of likes.')
                        break

    # close advertisement popup
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    # close match popup
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    # close out of likes popup
    def out_of_likes(self):
        out_of_likes = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        out_of_likes.click()


bot = TinderBot()
bot.login()
